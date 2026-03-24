from fastapi import FastAPI

from api.views import router
import settings


app = FastAPI(title="URL Shortener")

app.include_router(router)
