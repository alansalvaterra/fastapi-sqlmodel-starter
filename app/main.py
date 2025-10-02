from fastapi import FastAPI
from app.core.config import settings
from app.api.endpoints import itens 
from fastapi.middleware.cors import CORSMiddleware

# Cria aplicação FastAPI
app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    description="FastAPI SQLModel Starter Project", 
)

# Rotas
app.include_router(itens.router,  prefix=f"{settings.API_V1_STR}/itens",tags=["itens"])
# outros endpoints podem ser incluídos aqui

@app.get("/")
def root():
    """Rota inicial"""
    return {"message": "FastAPI SQLModel Starter Online!"}  # ← Mensagem genérica

@app.get("/health")
def health_check():
    """Health check da API"""
    return {"status": "healthy"}

# CORS (Comunicação entre frontend/backend)
if settings.ALLOWED_HOSTS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
else:
    # Em desenvolvimento, permite tudo
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )