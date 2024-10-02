import streamlit as st
import pandas as pd
import plotly.express as px
from langchain_openai import ChatOpenAI
import os

api_key = os.getenv("OPENAI_API_KEY")
chat = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=api_key
)

st.set_page_config(layout="wide")

df = pd.read_csv("finances.csv")
despesas_mensais = pd.read_csv("despesas_mensais.csv")
del df["ID"]
df["Mes"] = df["Data"].apply(lambda x: "-".join(x.split("-")[:-1]))
df["Data"] = pd.to_datetime(df["Data"])
df["Data"] = df["Data"].apply(lambda x: x.date())

def filter_data(df, mes, selected_categories):
    df_filtered = df[df['Mes'] == mes]
    if selected_categories:
        df_filtered = df_filtered[df_filtered['Categoria'].isin(selected_categories)]
    return df_filtered

if 'historico' not in st.session_state:
    st.session_state.historico = []

st.title("Dashboard de Finanças Pessoais")

st.sidebar.header("Filtros")
mes = st.sidebar.selectbox("Mês", df["Mes"].unique())
categories = df["Categoria"].unique().tolist()
selected_categories = st.sidebar.multiselect("Filtrar por Categorias", categories, default=categories)

df_filtered = filter_data(df, mes, selected_categories)

st.dataframe(df_filtered)

category_distribution = df_filtered.groupby("Categoria")["Valor"].sum().reset_index()
fig = px.pie(category_distribution, values='Valor', names='Categoria', title='Distribuição por Categoria', hole=0.3)
st.plotly_chart(fig, use_container_width=True)

st.sidebar.header("Chatbot Financeiro")
user_input = st.sidebar.text_input("Como posso ajudar você com suas finanças?")

if user_input:
    st.session_state.historico.append({"user": user_input})

    prompt_text = f"""
    Você é um assistente financeiro chamado Tommy. Abaixo estão algumas informações sobre as finanças:
    
    Total de gastos: R${df['Valor'].sum():,.2f}
    Resumo por categoria: {df.groupby('Categoria')['Valor'].sum().to_dict()}
    
    Despesas mensais: {despesas_mensais.to_dict(orient='records')}
    
    Histórico de conversas:
    {st.session_state.historico}

    Responda à pergunta a seguir com clareza e detalhe: {user_input}
    """
    
    response = chat.invoke(prompt_text)
    
    content = response.content if hasattr(response, 'content') else "Desculpe, não consegui entender a sua pergunta."
    
    st.session_state.historico.append({"chatbot": content})
    
    st.sidebar.write("Resposta do Chatbot:")
    st.sidebar.write(content)

    st.sidebar.write("Histórico de Conversas:")
    for entry in st.session_state.historico:
        if 'user' in entry:
            st.sidebar.write(f"Você: {entry['user']}")
        if 'chatbot' in entry:
            st.sidebar.write(f"Chatbot: {entry['chatbot']}")
