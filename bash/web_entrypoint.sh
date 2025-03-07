#!/bin/bash
set -e

echo "Ожидание доступности PostgreSQL на db:5432..."
while ! nc -z db 5432; do
    sleep 1
done

echo "Создаём миграции"
python manage.py makemigrations api --noinput

echo "Применяем миграции..."
python manage.py migrate --noinput

echo "Запускаем Gunicorn..."
exec gunicorn core.asgi:application -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000