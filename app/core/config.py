import os
from dotenv import load_dotenv
from typing import List

# Carrega .env
load_dotenv()

class Settings:
    """Configurações que mudam entre dev e prod"""
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    
    # App
    API_V1_STR: str = os.getenv("API_V1_STR", "/api/v1")
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "Investimentos API")
    
    # Segurança
    SECRET_KEY: str = os.getenv("SECRET_KEY", "chave-dev-fraca")
    DEBUG: bool = os.getenv("DEBUG", "true").lower() == "true"
    
    # CORS
    ALLOWED_HOSTS: List[str] = [
        host.strip() for host in os.getenv("ALLOWED_HOSTS", "").split(",") 
        if host.strip()
    ]

    @property
    def is_production(self):
        return not self.DEBUG

settings = Settings()