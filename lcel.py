from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from langchain_huggingface import ChatHuggingFace

from dotenv import load_dotenv


load_dotenv()

if __name__ == "__main__":
    prompt_content = "Tell me a joke aboue {topic}. Be brief and concise."
    topic = "ice cream"

    prompt = ChatPromptTemplate.from_template(prompt_content)
    model = ChatHuggingFace()
    output_parser = StrOutputParser()

    # compose a chain using pipes (like in terminal)
    # chain flows from Left to Right
    chain = prompt | model | output_parser

    # everything has .invoke() (they implement Runnable)
    print(f"chain.invoke(): {chain.invoke(input={"topic": topic})}")
    print(f"prompt.invoke(): {prompt.invoke(input={"topic": topic})}")
    print(f"model.invoke(): {model.invoke(HumanMessage(content=prompt_content))}")
