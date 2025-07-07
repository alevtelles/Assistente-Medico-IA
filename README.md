# 🩺 Assistente Virtual Médico com IA - Solução Baseada em RAG

Este aplicativo é um chatbot médico que utiliza a técnica de RAG (Retrieval Augmented Generation) para fornecer respostas precisas e relevantes a partir de documentos médicos carregados pelo usuário. O sistema realiza uma recuperação de informações (retrieval) e as utiliza como contexto para gerar respostas contextualmente mais robustas, minimizando erros e aumentando a assertividade nas respostas médicas.



## 🙋🏽 O que é RAG
RAG (Retrieval Augmented Generation) é uma técnica que aprimora modelos de linguagem integrando informações externas relevantes de uma base de dados ou documentos. Isso ajuda a evitar erros de geração (conhecidos como "alucinações") e a garantir respostas mais precisas, especialmente em domínios complexos e especializados como a medicina.

---

## ⚙️ Arquitetura

```
User Input
   ↓
Query Embedding → Pinecone Vector DB ← Embedded Chunks ← Chunking ← PDF Loader
   ↓
Retrieved Docs
   ↓
     RAG Chain (Groq + LangChain)
   ↓
LLM-generated Answer

```
- Entrada do Usuário: O usuário faz uma consulta ao sistema.
- Embedding da Consulta: A consulta é convertida em embeddings para facilitar a recuperação de documentos relevantes.
- Banco de Dados Vetorial (Pinecone): Armazena vetores de documentos e permite a recuperação eficiente de informações.
- RAG Chain: Processa a consulta, acessando o modelo LLaMA3-70B da Groq através do LangChain para gerar respostas baseadas no conteúdo recuperado.
- Resposta Gerada pelo LLM: O modelo gera uma resposta contextualizada utilizando o conhecimento recuperado.


## 📋 Funcionalidades

- Carregamento de PDFs Médicos: Suporte para upload de documentos médicos em formato PDF (notas, livros, relatórios, etc.).
- Extração Automática de Texto: O conteúdo dos PDFs é extraído automaticamente e fragmentado em blocos semânticos para facilitar a recuperação.
- Embedding de Conteúdo: O texto extraído é transformado em embeddings usando Google/BGE para otimizar a recuperação de informações.
- Armazenamento de Vetores: Os vetores gerados são armazenados na base de dados vetorial Pinecone, permitindo buscas rápidas e precisas.
- Uso do LLaMA3-70B: Utilização do modelo LLaMA3-70B da Groq para gerar respostas baseadas nos dados recuperados.
- Backend em FastAPI: API desenvolvida com FastAPI para gerenciamento de uploads de documentos e consultas (Q&A).

---

## 🚀 🚀 Tecnologias Utilizadas


| Tecnologia | Descrição |
|------------|-----------|
| Backend | FastAPI (framework assíncrono para APIs rápidas) |
| LLM | API Groq (LLaMA3-70B) |
| Embeddings | Google Generative AI / BGE |
| Vector DB | 	Pinecone (armazenamento de vetores) |
| Framework | LangChain (integração de RAG com LLaMA3-70B) |
| Deploy | Render (opcional para deploy em nuvem)| 

---

## 🛣️ Rotas


```bash
POST /upload_pdfs/ --- Carregar um ou mais arquivos PDFs

POST /ask/ --- Rota de perguntas

```
- /upload_pdfs/: Endpoint responsável pelo carregamento dos PDFs médicos, realizando a extração e fragmentação automática do conteúdo.

- /ask/: Endpoint para enviar uma pergunta ao assistente, que utiliza o conteúdo carregado para fornecer uma resposta baseada em dados factuais.
