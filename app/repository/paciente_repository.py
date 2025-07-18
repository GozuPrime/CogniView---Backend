# from config.supabase import supabase
from app.domain.paciente.paciente import Paciente,PacienteResponse

def create_paciente(datos:PacienteResponse):
    print(datos)