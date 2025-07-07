from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_llm_chain(retriever):
    llm=ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name='llama3-70b-8192'
    )

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=""""

        Você é **MediBot**, uma IA treinada para ajudar usuários a entender documentos médicos e questões relacionadas à saúde.

        Seu trabalho é fornecer respostas claras, precisas e úteis **com base apenas no contexto fornecido**.

        
        ---

        🔍 **Context**:
        {context}

        🙋🏽‍♂️ **Pergunta do Usuário**:
        {question}

        💬 **Respostas**
        IMPORTANTE:
        - Sempre responda em **português do Brasil**.
        - Responda de forma calma, factual e respeitosa.
        - Use explicações simples sempre que necessário.
        - Se o contexto não contiver a resposta, diga: "Desculpe, não encontrei informações relevantes nos documentos fornecidos."
        - NÃO invente fatos.
        - NÃO dê conselhos médicos ou diagnósticos.
        
        """,
    )

    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True,
    )