import re
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


class OlammaLLM:
    # Chat-only template
    chat_template = """
    You are a desktop assistant chatbot designed to help users with their queries. 
    If the user asks for clarification or further details, feel free to elaborate.
    Provide only textual responses to the questions asked in chat without any programming language source code even if the user asks for it.
    Conversation history: 
    {context}

    User's current question: 
    {question}

    Your response:
    """

    # Code-only template
    code_template = """
    You are a coding assistant designed to help users with their programming questions. 
    If the user asks for clarification or further details, feel free to elaborate.
    Provide only programming language source code. Do not include any additional text or attributes or labels.
    Do not include any decorators or programming language name as comment in the response. 

    
    If the code cannot be generated return 'error'
     
    User's question: 
    {question}
    
     

    Respond with only the source code without any other attributes. 
    """

    # File extension template
    file_extension_template = """
    You are an assistant that identifies the file extension based on the provided source code.
    Respond with only the file extension (e.g., .py, .js, .java). Do not include any additional text or explanations.

    Supported languages and their extensions:
    - Python: .py
    - JavaScript: .js
    - Java: .java
    - C++: .cpp
    - C: .c
    - C#: .cs
    - Ruby: .rb
    - HTML: .html
    - CSS: .css
    - SQL: .sql
    - PHP: .php
    - Swift: .swift
    - Go: .go
    - Kotlin: .kt
    - R: .r
    - Shell Script: .sh
    - Perl: .pl
    - MATLAB: .m
    - TypeScript: .ts
    - Scala: .scala
    - Lua: .lua
    - Julia: .jl
    - Rust: .rs
    - Haskell: .hs
    - Dart: .dart
    - Visual Basic .NET: .vb
    - Objective-C: .m
    - Groovy: .groovy
    - Tcl: .tcl
    - Fortran: .f90
    - Lisp: .lisp
    - Scheme: .scm
    - Prolog: .pl
    - CoffeeScript: .coffee
    - Assembly: .asm
    - Markdown: .md
    - YAML: .yml
    - JSON: .json
    - Verilog: .v
    - VHDL: .vhdl
    - Smalltalk: .st
    - Crystal: .cr
    - Elm: .elm
    - Solidity: .sol
    - XQuery: .xq
    - Q (Kdb+): .q
    - APL: .apl
    - COBOL: .cbl
    - Ada: .adb
    
    If the language cannot be identified, respond with '.txt'.  

    Provided source code:
    {source_code}
     
    Respond with only the file extension. 
    """

    # Model for chat, code, and file extension responses
    model = OllamaLLM(model="gemma:2b")

    # Create prompts
    chat_prompt = ChatPromptTemplate.from_template(chat_template)
    code_prompt = ChatPromptTemplate.from_template(code_template)
    file_extension_prompt = ChatPromptTemplate.from_template(file_extension_template)

    # Create chains
    chat_chain = chat_prompt | model
    code_chain = code_prompt | model
    file_extension_chain = file_extension_prompt | model


    @staticmethod
    def is_code_query(query: str):
        # List of keywords indicating a code-related query
        code_keywords = [
            "code", "script", "syntax", "function", "class", "loop", "variable",
            "compile", "execute", "algorithm", "debug", "error", "exception",
            "framework", "library", "API", "program"
        ]

        # Escape each keyword to handle special characters
        escaped_keywords = [re.escape(keyword) for keyword in code_keywords]

        # Check if any of the keywords are present in the query (case-insensitive)
        for keyword in escaped_keywords:
            if re.search(rf'\b{keyword}\b', query, re.IGNORECASE):
                return True
        return False

    @staticmethod
    def handle_conversation(query: str):
        context = ""

        # Identify whether the query is code-related
        if OlammaLLM.is_code_query(query):
            result = OlammaLLM.code_chain.invoke({"context": context, "question": query})

        else:
            result = OlammaLLM.chat_chain.invoke({"context": context, "question": query})

        return result

    @staticmethod
    def handle_file_extension(query: str):
        # Invoke the file extension identification chain
        result = OlammaLLM.file_extension_chain.invoke({"source_code": query})
        return result

    @staticmethod
    def format_llm_response(response):
        # Split the response into lines
        lines = response.strip().splitlines()

        # Remove the first and last lines
        if len(lines) > 2:
            lines = lines[1:-1]

        # Join the remaining lines back into a string
        formatted_response = "\n".join(lines)

        return formatted_response.strip()



# Example usage
if __name__ == "__main__":
    user_query = input("Enter your question: ")

    # Determine the response type
    response = OlammaLLM.handle_conversation(user_query)
    res = OlammaLLM.format_llm_response(response)
    print(res)

