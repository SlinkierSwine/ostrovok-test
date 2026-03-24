import logging
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: int = 0


def setup_logging(level: str):
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )


settings = Settings()
if settings.DEBUG:
    setup_logging('DEBUG')
else:
    setup_logging('INFO')

