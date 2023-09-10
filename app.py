import os
import streamlit as st
from langchain import OpenAI, LLMMathChain
from dotenv import load_dotenv



load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class MathSolverApp:
    def __init__(self):
        self.llm = OpenAI(temperature=0)
        self.llm_math = LLMMathChain.from_llm(self.llm, verbose=True)
        self.initialize_interface()

    def initialize_interface(self):
        st.title("Math Solver")
        st.sidebar.header("Instructions")
        st.sidebar.text("Pass your math query in the text box and tap on 'Execute' to get desired result.")
        
        query = st.text_input("Kindly pass your Math query:")
        execute_button = st.button("Execute")

        if execute_button:
            if query:
                self.execute_query(query)
            else:
                st.error("Enter a valid math query!")

    def execute_query(self, query):
        try:
            result = self.llm_math.run(query)
            st.success("Executed Successfully")
            st.write("Result:", result)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = MathSolverApp()
