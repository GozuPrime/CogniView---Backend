from fastapi import APIRouter
from app.domain.paciente.paciente import Paciente,PacienteResponse
from app.repository.paciente_repository import create_paciente
import logging

paciente_route = APIRouter()
logging = logging.getLogger("uvicorn")


@paciente_route.get('/',summary="Listar los pacientes", description="""
Devuelve una lista de paciente.
""")
def paciente_sellst():
    return {"d":"helo"}


@paciente_route.post('/',summary="Crear paciente", description="""
Devuelve al paciente registrado
""")
def paciente_inst(datos:PacienteResponse):
    return create_paciente(datos=datos)

@paciente_route.delete('/{id}',summary="Eliminar paciente", description="""
Devuelve al paciente eliminadno
""")
def paciente_dlt(id:int):
    return id

@paciente_route.delete('/{id}',summary="Eliminar paciente", description="""
Devuelve al paciente eliminadno
""")
def paciente_dlt(id:int):
    return id

@paciente_route.get('/{id}',summary="Buscar paciente", description="""
Devuelve al paciente buscado
""")
def paciente_get(id:int):
    return id

@paciente_route.put('/{id}',summary="Actualizar paciente", description="""
Devuelve al paciente actualizado
""")
def paciente_dlt(id:int,datos:PacienteResponse):
    return id



