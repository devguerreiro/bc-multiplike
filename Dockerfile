FROM python:3.10

ENV WORKDIR=/multiplike_backend

WORKDIR ${WORKDIR}

RUN pip3 install poetry

COPY pyproject.toml ${WORKDIR}/

RUN poetry export -f requirements.txt -o requirements.txt --without-hashes

COPY app ${WORKDIR}/app

RUN pip3 install -r requirements.txt

EXPOSE 8080

ENTRYPOINT uvicorn app.infra.api:app --host 0.0.0.0 --port 8080