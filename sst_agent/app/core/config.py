"""Centralized application settings."""

from dotenv import load_dotenv
import os
from sqlalchemy.engine import URL


load_dotenv()

PROJECT_NAME = "SST Agent"
VERSION = "0.1"
DEBUG = os.getenv("DEBUG", "false").lower() in {"1", "true", "yes", "on"}

# Groq API
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

def build_database_url() -> str:
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        return database_url

    username = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "postgres")
    host = os.getenv("POSTGRES_HOST", "db")
    port = int(os.getenv("POSTGRES_PORT", "5432"))
    database = os.getenv("POSTGRES_DB", "sst_agent")

    return URL.create(
        "postgresql+psycopg2",
        username=username,
        password=password,
        host=host,
        port=port,
        database=database,
    ).render_as_string(hide_password=False)


DATABASE_URL = build_database_url()
DB_DDL_AUTO = os.getenv("DB_DDL_AUTO", "create").strip().lower()

# Embeddings
EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/all-MiniLM-L6-v2",
)
EMBEDDING_DIMENSION = int(os.getenv("EMBEDDING_DIMENSION", "384"))
ALLOWED_ORIGINS = [
    origin.strip()
    for origin in os.getenv(
        "ALLOWED_ORIGINS",
        "http://localhost:3002,http://127.0.0.1:3002",
    ).split(",")
    if origin.strip()
]
