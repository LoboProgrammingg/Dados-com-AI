# Dashboard de Finanças Pessoais com Chatbot Inteligente

**Este projeto é uma solução para analisar e visualizar dados dos extratos do seu Banco, utilizando inteligência artificial para gerar descrições ideais para cada transação. O objetivo é oferecer um assistente financeiro que ajude os usuários a gerenciar melhor suas finanças.**

## Como o Projeto vai ficar:
![alt text](image.png)

## Tecnologias Utilizadas

- **Streamlit**: Para criar um dashboard interativo e de fácil uso.
- **Pandas**: Para leitura e manipulação de dados.
- **Plotly**: Para visualização gráfica dos dados financeiros.
- **Langchain**: Para integração com a API da OpenAI, criando um chatbot inteligente capaz de responder perguntas sobre finanças.
- **OpenAI API**: Para utilização de modelos de linguagem avançados.

## Funcionalidades

- **Leitura de Extratos**: O sistema lê extratos financeiros a partir de arquivos CSV.
- **Descrição Inteligente**: Utiliza IA para gerar descrições detalhadas das transações.
- **Dashboard Interativo**: Visualize seus dados em gráficos e tabelas para melhor compreensão das suas finanças.
- **Chatbot Financeiro**: Um assistente que pode responder perguntas sobre seus gastos e oferecer dicas sobre gerenciamento financeiro, com histórico de interações.
- **Filtragem de Dados**: Possibilidade de filtrar transações por mês e categoria.

## Instruções para Uso

### Pré-requisitos

1. **Python**: Certifique-se de ter o Python instalado na sua máquina. Recomenda-se usar a versão 3.7 ou superior.
2. **Pacotes Necessários**: Instale as seguintes bibliotecas usando pip:
   ```bash
   pip install streamlit pandas plotly langchain-openai
3.  **API da OpenAI**: Para utilizar o chatbot, você precisará de uma chave da API da OpenAI. Cadastre-se em OpenAI e obtenha sua chave.

### Configuração dos Dados
1. #### Preparacao dos Arquivos CSV:
    + **Crie uma pasta chamada extrato no diretório do seu projeto.**
    + **Coloque seus arquivos CSV dos extratos do Banco do Brasil na pasta extrato.**
    + **O projeto requer pelo menos dois arquivos CSV:**
        + finances.csv: Contendo os dados principais das transações
        + despesas_mensais.csv: Contendo informações sobre despesas mensais.
2. #### Configuração do Ambiente:
    + **Crie um arquivo .env no diretório do seu projeto e adicione sua chave da API:**
    ```bash
    API_OPENAI_KEY=YOUR_API_KEY
### Executando o Projeto
1. #### Navegue até o diretório do projeto no terminal.
2. #### Execute o seguinte comando para iniciar o Streamlit:
    ```bash
    streamlit run app.py
3. #### O aplicativo será iniciado e abrirá automaticamente uma nova aba no seu navegador.

### Interagindo com o ChatBot
+ **No painel lateral, você encontrará um campo para enviar perguntas ao chatbot.**
+ **O assistente pode responder a perguntas sobre suas finanças e fornecer dicas sobre como gerenciar melhor seu dinheiro.**

### Notas de Segurança
+ **Por motivos de segurança, não compartilharei os arquivos CSV e a pasta extrato no GitHub. Certifique-se de manter seus dados financeiros protegidos e nunca compartilhe informações sensíveis publicamente.**

### CREATED BY:
- **|Matheus Lobo Camara|**