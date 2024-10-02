import ofxparse
import pandas as pd
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers.string import StrOutputParser
import os

df = pd.DataFrame()
for extrato in os.listdir("extratos"):
    with open(f'extratos/{extrato}', encoding='ISO-8859-1') as ofx_file:
        ofx = ofxparse.OfxParser.parse(ofx_file)
    transactions_data = []
    for account in ofx.accounts:
        for transaction in account.statement.transactions:
            transactions_data.append({
                "Data": transaction.date,
                "Valor": transaction.amount,
                "Descricao": transaction.memo,
                "ID": transaction.id
            })
            
    df_temp = pd.DataFrame(transactions_data)
    df_temp["Valor"] = pd.to_numeric(df_temp["Valor"], errors='coerce')
    df_temp['Data'] = df_temp['Data'].apply(lambda x: x.date())
    df = pd.concat([df, df_temp])


template = """
Voce sera uma analista de dados, trabalhando em um projeto de limpeza de dados.
Seu trabalho sera escolher uma categoria adequada para cada lancamento financeiro
que vou te enviar eu quero tambem que voce crie uma tabela de despesas e informe
quanto o usuario gastou naquele mes.

Todos sao transacoes financeiras de uma pessoa fisica.

Escolha uma dentre as seguintes categorias:
- Alimentacao
- Saude
- Educacao
- Bares
- Festas
- Investimento
- Transferencia para terceiros
- Pix recebido
- Pix enviado
- Telefone
- Academia
- Lazer
- Saude
- Mercado

Escolha a categoria deste item:
{text}

Responda apenas com a categoria.
"""

prompt = PromptTemplate.from_template(template=template)

api_key = os.getenv("OPENAI_API_KEY")
chat = ChatOpenAI(
    model="gpt-4o",
    api_key=api_key
)

chain = prompt | chat | StrOutputParser()

categorias = chain.batch(list(df["Descricao"].values))
df["Categoria"] = categorias

df.to_csv("financas.csv", index=False)


