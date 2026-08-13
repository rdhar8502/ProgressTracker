from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://tracker:tracker123@db:5432/progress_tracker"
    APP_ENV: str = "development"
    SECRET_KEY: str = "supersecretkey123changeme"

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
