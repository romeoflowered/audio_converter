#!/bin/zsh

alembic upgrade head

gunicorn audio_converter.main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
