# Podcast Editor

This repository contains the web editor and the private Python service that will
process audio.

```text
web/  Svelte + Vite interface
api/  FastAPI + pyannote.audio service
```

## Web app

From the repository root:

```sh
pnpm install
pnpm dev
```

The web app is available at the URL printed by Vite (normally
`http://localhost:5173`).

## Python API

Create an isolated Python environment once:

```sh
cd api
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
cp .env.example .env
```

Set your real Hugging Face token in `api/.env`. This file is ignored by Git.

Start the API from the repository root:

```sh
pnpm api:dev
```

It exposes a basic health endpoint at `http://127.0.0.1:8000/health`.

The next implementation step is an authenticated audio-analysis endpoint that
uses `HF_TOKEN` server-side and returns speaker/time segments to `web/`.
