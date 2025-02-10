from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://qasim:123456@localhost:5432/course_db"

    class Config:
        env_file = ".env"

settings = Settings()