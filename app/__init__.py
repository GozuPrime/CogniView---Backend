from fastapi import FastAPI
from .routes.paciente_routes import paciente_route

def create_app():
    app = FastAPI(title="CogniView API", version="1.0.0")

    # REGISTRO DE LAS RUTAS
    app.include_router(paciente_route,prefix="/paciente",tags=["Paciente"])

    return app