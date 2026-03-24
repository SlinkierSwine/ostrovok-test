from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = 'URL Shortener'
    DEBUG: int = 0
    DATABASE_URL: str = 'postgresql://user:password@db:5432/url_shortener'

