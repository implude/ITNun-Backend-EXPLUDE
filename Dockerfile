FROM python:3.8-slim

COPY ./src /src
COPY ./requirements.txt /requirements.txt
COPY ./.env /src/.env

RUN pip3 install -r requirements.txt

WORKDIR /src

ENV FLASK_DEBUG=1

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]