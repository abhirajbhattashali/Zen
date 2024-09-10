
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

class OlammaLLM:
    template = """
    You are an intelligent assistant designed to help users with their queries. 
    Provide thoughtful, concise, and helpful responses. If the user asks 
    for clarification or further details, feel free to elaborate.
    Conversation history: 
    {context}

    User's current question: 
    {question}

    Your response:
    """

    model = OllamaLLM(model="gemma:2b")

    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    @staticmethod
    def handle_conversation(query:str):
        context = ""
        result = OlammaLLM.chain.invoke({"context":context, "question": query})
        return result

