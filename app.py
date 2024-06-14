import streamlit as st
import pandas as pd
import os
import nest_asyncio
from llama_index.llms.anthropic import Anthropic
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.query_pipeline import (
    QueryPipeline as QP,
    Link,
    InputComponent,
)
from llama_index.experimental.query_engine.pandas import PandasInstructionParser
from llama_index.core.prompts import PromptTemplate

# Apply nest_asyncio for running async code in Streamlit
nest_asyncio.apply()

# Set up environment variables for API keys
os.environ["LLAMA_CLOUD_API_KEY"] = ""
os.environ["ANTHROPIC_API_KEY"] = ""

# Streamlit interface
st.title("NY House Dataset Query Interface")
# Display the image
st.image(r"C:\Users\ibrahim\Desktop\projects\real_estate_LLM\env\property.jpg",  use_column_width=True)

# File upload and dataset loading in the sidebar
uploaded_file = st.sidebar.file_uploader("Upload a CSV file 📂", type=["csv"])

# Main content area
st.title("Dataset Explorer 📊")

# Load the dataset
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Dataset Preview:")
    st.write(df.head())  # Display the first few rows of the dataset
else:
    st.write("Please upload a CSV file.")  # Prompt to upload a CSV file if none is uploaded

if uploaded_file is not None and df is not None:
    # Define prompt templates
    instruction_str = (
        "1. Convert the query to executable Python code using Pandas.\n"
        "2. The final line of code should be a Python expression that can be called with the `eval()` function.\n"
        "3. The code should represent a solution to the query.\n"
        "4. PRINT ONLY THE EXPRESSION.\n"
        "5. Do not quote the expression.\n"
    )

    pandas_prompt_str = (
        "You are working with a pandas dataframe in Python.\n"
        "The name of the dataframe is `df`.\n"
        "This is the result of `print(df.head())`:\n"
        "{df_str}\n\n"
        "Follow these instructions:\n"
        "{instruction_str}\n"
        "Query: {query_str}\n\n"
        "Expression:"
    )
    response_synthesis_prompt_str = (
        "Given an input question, synthesize a response from the query results.\n"
        "Query: {query_str}\n\n"
        "Pandas Instructions (optional):\n{pandas_instructions}\n\n"
        "Pandas Output: {pandas_output}\n\n"
        "Response: "
    )

    # Prepare prompts with the initial data
    pandas_prompt = PromptTemplate(pandas_prompt_str).partial_format(
        instruction_str=instruction_str, df_str=df.head(5)
    )
    pandas_output_parser = PandasInstructionParser(df)
    response_synthesis_prompt = PromptTemplate(response_synthesis_prompt_str)

    # Initialize the language model
    llm = Anthropic(model="claude-2.1", temperature=0.1)

    # Set up the query pipeline
    qp = QP(
    modules={
        "input": InputComponent(),
        "pandas_prompt": pandas_prompt,
        "llm1": llm,
        "pandas_output_parser": pandas_output_parser,
        "response_synthesis_prompt": response_synthesis_prompt,
        "llm2": llm,
    },
    verbose=True,
)
qp.add_chain(["input", "pandas_prompt", "llm1", "pandas_output_parser"])
qp.add_links(
    [
        Link("input", "response_synthesis_prompt", dest_key="query_str"),
        Link(
            "llm1", "response_synthesis_prompt", dest_key="pandas_instructions"
        ),
        Link(
            "pandas_output_parser",
            "response_synthesis_prompt",
            dest_key="pandas_output",
        ),
    ]
)
# add link from response synthesis prompt to llm2
qp.add_link("response_synthesis_prompt", "llm2")

query = st.text_input("Enter your query:")

response = qp.run(query_str=query)
st.write (response.message.content.strip())

  
