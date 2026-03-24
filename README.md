# Url shortener
Простой сервис для сокращения ссылок. Использует 6 символов `uuid.hex` для создания короткой ссылки.

## Стек
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Docker, Docker Compose
- Pytest

## Запуск
```bash
docker compose up --build
```
Все нужные `env` переменные прописаны в `docker-compose.yml`
Сервер запустится на `http://localhost:8000`

## Тесты
```bash
docker compose exec app pytest
или
docker compose run app pytest
```

## API
- POST /shorten - создание сокращенной ссылки 
- GET /{short_id} - редирект по оригинальной ссылке
- GET /stats/{short_id} - получение статистики (количества кликов) по ссылке
