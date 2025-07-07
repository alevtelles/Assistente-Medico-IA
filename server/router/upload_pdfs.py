from fastapi import APIRouter, UploadFile, File
from typing import List
from modules.load_vectorstore import load_vectorstore
from fastapi.responses import JSONResponse
from logger import logger


router=APIRouter()

@router.post("/upload_pdfs")
async def upload_pdfs(files:List[UploadFile] = File(...)):
    try:
        logger.info("Arquivos de upload recebidos")
        load_vectorstore(files)
        logger.info("Documento adicionado ao repositório vetorial")
        return {"message": "Arquivo processado e repositório vetorial atualizado"}
    except Exception as e:
        logger.exception("Erro durante o upload do PDF")
        return JSONResponse(status_code=500, content={"error":str(e)})