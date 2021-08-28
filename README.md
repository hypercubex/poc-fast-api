# README

Kafka setup referenced from this tutorial<https://www.baeldung.com/ops/kafka-docker-setup>

## How to start

1. Please rename .env.example to .env
1. `docker compose up --build -d` (topic 'transactions', database 'test' with table 'transactions' will be created automatically)
1. `pipenv install`
1. `cd src`
1. `pipenv run uvicorn main:app --reload`
1. access <http://localhost:8000/transactions> to operate
