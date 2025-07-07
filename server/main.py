from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middlewares.exception_handlers import catch_exception_middleware
from router.upload_pdfs import router as upload_router
from router.ask_question import router as ask_router


app = FastAPI(
    title="Assistente Médico Virtual",
    description="API inteligente para chatbot médico, oferecendo respostas automáticas com tecnologia de IA.",
)

# CORS Configuração
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

# Middleware exception handlers
app.middleware("http")(catch_exception_middleware)

# routers


# 1. upload pdfs documents
app.include_router(upload_router)

# 2. asking query
app.include_router(ask_router)