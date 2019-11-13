FROM jfloff/alpine-python:3.7

LABEL maintainer "matthewgleich@gmail.com"
LABEL description "Look on https://github.com/Matt-Gleich/Auto-Doc-Dockerfiles/README.md"

# Installing Dependecies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src src

WORKDIR /src

CMD [ "python3", "main.py" ]
