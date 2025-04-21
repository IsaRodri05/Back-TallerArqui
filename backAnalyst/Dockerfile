FROM python:3

RUN apt-get update && apt-get install -y netcat-traditional

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

CMD ["sh", "docker-entrypoint.sh"]