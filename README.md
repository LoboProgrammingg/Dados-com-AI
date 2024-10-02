# Personal Finance Dashboard with Intelligent Chatbot

**This project is a solution to analyze and visualize data from your bank statements, using artificial intelligence to generate ideal descriptions for each transaction. The goal is to provide a financial assistant that helps users better manage their finances.**

## How the Project Will Look:
![image](https://github.com/user-attachments/assets/f782650e-3750-4e78-949a-70aed7fdbec8)


## Technologies Used

- **Streamlit**: To create an interactive and user-friendly dashboard.
- **Pandas**: For reading and manipulating data.
- **Plotly**: For graphical visualization of financial data.
- **Langchain**: For integration with the OpenAI API, creating an intelligent chatbot capable of answering questions about finances.
- **OpenAI API**: For utilizing advanced language models.

## Features

- **Statement Reading:** O sistema lê extratos financeiros a partir de arquivos CSV.
- **Intelligent Description:** Utiliza IA para gerar descrições detalhadas das transações.
- **Interactive Dashboard:** Visualize seus dados em gráficos e tabelas para melhor compreensão das suas finanças.
- **Financial Chatbot:** Um assistente que pode responder perguntas sobre seus gastos e oferecer dicas sobre gerenciamento financeiro, com histórico de interações.
- **Data Filtering** Possibilidade de filtrar transações por mês e categoria.

## Instructions for Use

### Prerequisites

1. **Python**: Ensure you have Python installed on your machine. It is recommended to use version 3.7 or higher.
2. **Pacotes Necessários**: Install the following libraries using pip:
   ```bash
   pip install streamlit pandas plotly langchain-openai
3.  **API da OpenAI**: To use the chatbot, you will need an OpenAI API key. Sign up on OpenAI and obtain your key.

### Data Setup
1. #### Preparing CSV Files:
    + **Create a folder named 'extrato' in your project directory.**
    + **Place your bank statement CSV files in the 'extrato' folder.**
    + **The project requires at least two CSV files:**
        + finances.csv: Containing the main transaction data
        + despesas_mensais.csv: Containing information about monthly expenses.
2. #### Environment Setup:
    + **Create a .env file in your project directory and add your API key:**
    ```bash
    API_OPENAI_KEY=YOUR_API_KEY
### Running the Project
1. #### Navigate to the project directory in your terminal.
2. #### Run the following command to start Streamlit:
    ```bash
    streamlit run app.py
3. #### The application will start and automatically open a new tab in your browser.

### Interacting with the Chatbot
+ **NIn the sidebar, you will find a field to send questions to the chatbot.**
+ **The assistant can answer questions about your finances and provide tips on how to better manage your money.**

### Security Notes
+ **For security reasons, I will not share the CSV files and the 'extrato' folder on GitHub. Ensure that you keep your financial data protected and never share sensitive information publicly.**

### CREATED BY:
- **|Matheus Lobo Camara|**
