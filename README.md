

# 🏡 NY House Dataset Query Interface

This project is an interactive web application built with Streamlit that allows users to upload a CSV file containing New York real estate data and query it using natural language. The app leverages the power of Large Language Models (LLMs) and Anthropic's Claude to generate Python code that performs the requested data manipulations on the uploaded dataset.

## 🌟 Features

- 📂 Upload a CSV file containing New York real estate data.
- 🖼️ View a preview of the uploaded dataset.
- 💬 Enter natural language queries to manipulate and analyze the dataset.
- 🛠️ Generate and execute Python code to answer the queries.
- 📊 Display the results of the queries in the app.

## 🛠️ Requirements

- Python 3.7 or higher
- Streamlit
- Pandas
- nest_asyncio
- llama_index
- anthropic

## 📥 Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/abraham3333/LLM_Pandas_Real_Estate.git
    cd LLM_Pandas_Real_Estate
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv env
    source env/bin/activate   # On Windows, use `env\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables for the API keys in a `.env` file:

    ```env
    LLAMA_CLOUD_API_KEY=your_llama_cloud_api_key
    ANTHROPIC_API_KEY=your_anthropic_api_key
    ```

5. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

## 🚀 Usage

1. Upload a CSV file containing New York real estate data using the file uploader in the sidebar.
2. View a preview of the dataset in the main content area.
3. Enter your query in the text input box. For example, "What is the average price of houses in Manhattan?"
4. The app will generate and execute Python code to answer your query and display the results.

## 📝 Code Explanation

The `app.py` file contains the main code for the Streamlit application:

- **Import Libraries**: Necessary libraries like Streamlit, Pandas, nest_asyncio, and llama_index are imported.
- **Apply nest_asyncio**: This is needed to run asynchronous code in Streamlit.
- **Set Up Environment Variables**: API keys for LLAMA and Anthropic are set up.
- **Streamlit Interface**: The main Streamlit interface is set up, including title, image display, and file uploader.
- **Dataset Loading**: The uploaded CSV file is loaded and a preview is displayed.
- **Query Pipeline Setup**: The query pipeline is set up using the Llama Index library to handle natural language queries and generate corresponding Python code.
- **Query Execution**: The entered query is processed, and the result is displayed.

## 🤝 Contributing

Feel free to fork this repository and submit pull requests. For any issues or feature requests, please open an issue on the GitHub repository.

## 📜 License

This project is licensed under the MIT License.

## 🙏 Acknowledgements

- [Streamlit](https://www.streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Anthropic](https://www.anthropic.com/)

---

This README provides an overview of the project, installation instructions, usage guidelines, and other relevant information. Let me know if there's anything else you would like to add!
