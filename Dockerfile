FROM python:3.6.9

LABEL Author="Matteo Scarpello"
LABEL E-mail="m.scarpello@2hire.io"
LABEL version="0.0.1"

ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app
WORKDIR /app

COPY Pip* /app/

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --dev --system --deploy --ignore-pipfile

EXPOSE 8080

CMD waitress-serve --call flask_be_template:create_app