from fastapi import FastAPI

from api.views import router
from config import settings, logging


if settings.DEBUG:
    logging.setup_logging('DEBUG')
else:
    logging.setup_logging('INFO')

app = FastAPI(title=settings.APP_NAME)

app.include_router(router)

