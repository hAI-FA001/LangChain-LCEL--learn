from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

from dotenv import load_dotenv


load_dotenv()

if __name__ == "__main__":
    model_repo = "microsoft/Phi-3-mini-4k-instruct"
    prompt_content = "Tell me a joke aboue {topic}. Be brief and concise."
    topic = "ice cream"

    prompt = ChatPromptTemplate.from_template(prompt_content)
    model = ChatHuggingFace(llm=HuggingFaceEndpoint(repo_id=model_repo, task="text-generation", max_new_tokens=512))
    output_parser = StrOutputParser()

    # compose a chain using pipes (like in terminal)
    # chain flows from Left to Right
    chain = prompt | model | output_parser

    # everything has .invoke() (they implement Runnable)
    print(f"chain.invoke(): {chain.invoke(input={"topic": topic})}")
    print(f"prompt.invoke(): {prompt.invoke(input={"topic": topic})}")
    print(f"model.invoke(): {model.invoke(prompt.invoke(input={"topic": topic}))}")
