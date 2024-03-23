FROM python:3.11-slim

COPY . /app
WORKDIR /app

RUN pip install poetry
RUN poetry lock && poetry install

EXPOSE 8000

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]