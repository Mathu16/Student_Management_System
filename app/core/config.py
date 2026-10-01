# Import BaseSettings to load configuration values from environment variables
from pydantic_settings import BaseSettings, SettingsConfigDict


# Create a settings class for our application configuration
class Settings(BaseSettings):

    # PostgreSQL database connection URL
    DATABASE_URL: str

    # Secret key used to create and verify JWT tokens
    JWT_SECRET: str

    # Algorithm used for JWT token encoding
    JWT_ALGORITHM: str = "HS256"

    # Token expiration time in minutes
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Application port number
    PORT: int = 8000

    # Tell Pydantic where to find the .env file
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


# Create one settings object that can be imported throughout the project
settings = Settings()