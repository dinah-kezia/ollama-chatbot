from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """ 
answer the quesrion below,

here is the conversation history: {context}

Question: {question} 

Answer: 
"""

llm = OllamaLLM(model ="llama-3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | llm

def handle_conversation():
    context = ""
    print("Welcome to ai chatbot! Type bye to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            break


        result = chain.invoke({"context": context, "question": user_input})
        print("Bot: ",result)

        context += F"\nUser: {user_input}\nAI: {result}"
        print(result)

if __name__ == "__main__":
    handle_conversation()