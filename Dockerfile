FROM python:3.8-slim

LABEL maintainer="https://github.com/Paulo-Lopes-Estevao"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /assinatura

COPY . /assinatura/

CMD [ "python", "signature.py" ]