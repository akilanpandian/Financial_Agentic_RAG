from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # API Configuration
    api_service_title: str
    api_version: str
    api_host: str = "0.0.0.0"
    api_port: int = 8081
    api_workers: int = 4

    # Ollama Configuration
    ollama_base_url: str

    # Vector DB Configuration
    vector_db_type: str
    chromadb_persist_directory: str
    chromadb_collection_name: str

    # RAG Configuration
    rag_chunk_size: int
    rag_chunk_overlap: int
    rag_top_k: int
    rag_similarity_threshold: float = 0.7
    rag_embedding_model: str = "nomic-embed-text"

    # Agent Configuration
    agent_llm_model: str = "qwen2.5:latest"
    agent_temperature: float = 0.3
    agent_max_tokens: int = 4096
    agent_max_iterations: int = 10
    agent_system_prompt: str = (
        "You are a senior financial analyst. "
        "When given financial statements and data, produce a structured, professional analysis. "
        "Cover: revenue and profit trends, cash flow health, balance sheet strength, "
        "key ratios (P/E, debt-to-equity, operating margin, ROE where data allows), "
        "and a concise investment summary with risks and outlook. "
        "Be factual, cite specific numbers, and base all conclusions strictly on the provided data."
    )

    # App Configuration
    environment: str = "development"
    debug: bool = False
    obs_log_level: str = "INFO"
    obs_log_format: str = "json"

    # Reads .env file automatically
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

def get_settings() -> Settings:
    return Settings()