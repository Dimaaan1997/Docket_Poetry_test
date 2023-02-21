FROM python:3.8.16
WORKDIR /app
RUN pip3 install poetry
COPY pyproject.toml poetry.lock README.md /app
RUN poetry config virtualenvs.create false && poetry install

COPY ./ /app
CMD ["uvicorn", "docker_poetry_test.main:app", "--host", "0.0.0.0", "--port", "80"]



