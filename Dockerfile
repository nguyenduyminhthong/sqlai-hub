FROM python:3.10

WORKDIR /app

COPY . .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt
