from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

llm = Ollama(model="gemma:2b")

prompt = PromptTemplate(
    input_variables=["chat_history", "user_input"],
    template="""
    Sei un assistente virtuale gentile, chiaro e professionale. Rispondi in modo semplice e comprensibile, anche per chi non è esperto.

    Conversazione finora:
    {chat_history}

    Utente: {user_input}
    Assistente:
    """
)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=False)

chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory,
    verbose=False
)

def chat(user_input: str):
    return chain.predict(user_input=user_input)
