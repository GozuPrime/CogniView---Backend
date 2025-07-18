from pydantic import BaseModel

class Paciente(BaseModel):
    idPaciente:str
    nombre:str
    apellido:str
    dni:str


class PacienteResponse(BaseModel):
    nombre:str
    apellido:str
    dni:str