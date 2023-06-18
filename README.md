
# Getting started

## It requires

- Python >=v3.10
- Poetry >=v1.4.2

## Setup

```bash
# Clone the project
$ git clone --depth 1 git@github.com:luisnquin/url-shortener-b

# Install dependencies
$ poetry install

# Start server
$ poetry run uvicorn url_shortener_b.main:app --reload

# Create a new short url
$ curl -sX POST http://127.0.0.1:8000/create -H 'Content-Type: application/json' -d '{"url": "https://google.com"}' | jq

# See endpoints documentation
$ xdg-open http://127.0.0.1:8000/docs
```
