# 🚀 FastAPI SQLModel Starter

Boilerplate profissional para APIs Python com FastAPI, SQLModel, PostgreSQL e Alembic.

## ✨ Características

- ✅ **FastAPI** com documentação automática Swagger
- ✅ **SQLModel** (SQLAlchemy + Pydantic) para modelos
- ✅ **PostgreSQL** com Docker para desenvolvimento
- ✅ **Alembic** para migrations do banco
- ✅ **CRUD completo** com exemplos práticos
- ✅ **Estrutura escalável** e profissional
- ✅ **Ambiente dev/prod** separado

## 📊 Modelo de Exemplo: `Item`

Tabela genérica que serve como base para:
- 🛒 **Produtos** (e-commerce)
- 👥 **Clientes** (CRM) 
- ✅ **Tarefas** (task manager)
- 📝 **Posts** (blog)
- 🎯 **Qualquer entidade** do seu projeto

**Campos:**
- `nome` - Identificador principal
- `descricao` - Detalhes opcionais  
- `preco` - Valor monetário (opcional)
- `quantidade` - Contador genérico
- `ativo` - Status booleano
- `criado_em` - Timestamp automático

## 🛠️ Como Usar

### 📋 Pré-requisitos
- Python 3.8+
- Docker e Docker Compose
- Git

### 🚀 Início Rápido

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/fastapi-sqlmodel-starter.git
cd fastapi-sqlmodel-starter

# 2. Crie e ative o ambiente virtual
python -m venv venv
# Linux/Mac:
source venv/bin/activate
# Windows:
.\venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Inicie o PostgreSQL com Docker
docker-compose up -d postgres

# 5. Execute as migrations do banco
alembic upgrade head

# 6. Popule com dados de exemplo
python scripts/seed_data.py

# 7. Inicie a API
uvicorn app.main:app --reload
```

### 🌐 Acesse a API

- **API**: http://localhost:8000
- **Documentação Swagger**: http://localhost:8000/docs  
- **Documentação Redoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

### 📚 Endpoints Disponíveis

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/v1/itens/` | Lista todos os itens |
| POST | `/api/v1/itens/` | Cria novo item |
| GET | `/api/v1/itens/{id}` | Busca item por ID |
| PUT | `/api/v1/itens/{id}` | Atualiza item completo |
| PATCH | `/api/v1/itens/{id}` | Atualiza item parcial |
| DELETE | `/api/v1/itens/{id}` | Deleta item |

**Desenvolvido com ❤️ usando FastAPI + SQLModel + PostgreSQL**