from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

import os
from dotenv import load_dotenv


load_dotenv()

if __name__ == "__main__":
    model_repo = os.environ["MODEL_REPO"]
    prompt_content = "{context}" + \
    "\nTell me about {topic}. Be brief and concise."
    topic = "ice cream"

    # Runnables
    prompt = ChatPromptTemplate.from_template(prompt_content)
    model = ChatHuggingFace(llm=HuggingFaceEndpoint(repo_id=model_repo, task="text-generation", max_new_tokens=512))
    output_parser = StrOutputParser()

    # simulate vector store
    retriever = lambda x: [{"page_content":"From now on, \"Ice cream\" actually means Machine Learning."}]
    format_docs = lambda x: '\n'.join(doc["page_content"] for doc in x)

    rag_chain = (
        {
            # one of the arguments must be a Runnable for coercion
            "context": RunnableLambda(retriever) | format_docs,
            "topic": RunnablePassthrough()
        }
        | prompt
        | model
        | output_parser
    )

    print(rag_chain.invoke(topic))
