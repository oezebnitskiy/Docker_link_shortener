FROM python:3.7
ADD . /code
WORKDIR /code
RUN pip install poetry
RUN poetry install
CMD  poetry run python3 ./docker_redis/app.py 