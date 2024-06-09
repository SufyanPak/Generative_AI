FROM python:3.12
LABEL maintainer = "Sufyan"
WORKDIR /code
RUN pip install poetry
COPY . /code/
# Configuration to avoid creating virtual environment inside the Docker Container"
RUN poetry config virtualenvs.create false
RUN poetry install
EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "fastapi_class1.main:app", "--reload"]
