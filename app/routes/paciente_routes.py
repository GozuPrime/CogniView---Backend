from fastapi import APIRouter
import logging

paciente_route = APIRouter()
logging = logging.getLogger("uvicorn")


@paciente_route.get('/',summary="Listar los pacientes", description="""
Devuelve una lista de paciente.
""")
def paciente_sellst():
    return {"d":"helo"}