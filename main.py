from fastapi import FastAPI
from routers import predict
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Cargar variables de entorno desde .env (opcional)
load_dotenv()

app = FastAPI(
    title="API de Riesgo de Morosidad",
    description="Predice si un cliente tiene alto riesgo de impago",
    version="1.0"
)

# CORS - Permite acceso desde el frontend o Postman
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ Cambia esto por ["http://localhost:3000"] si tienes frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar rutas
app.include_router(predict.router, prefix="/predict", tags=["Predicción"])

# Ruta raíz opcional
@app.get("/")
def read_root():
    return {"message": "API de riesgo activa y operativa"}
