# FastAPI + MongoDB Multi-Container Setup

A beginner-friendly Docker Compose project that runs a Python FastAPI application and MongoDB as separate containers on the same Docker network.

## Architecture

Browser / HTTP client → FastAPI (`python_app`, port 8000) → MongoDB (`mongo`, internal port 27017)

The application uses the Docker Compose service name `mongo` to connect to MongoDB. The database is not exposed to the host. A named volume preserves MongoDB data when containers restart.

## Requirements

- Docker Desktop with Docker Compose

## Run locally

1. Copy `.env.example` to `.env` and replace `replace_with_local_password` with a local password. Do not commit `.env`.
2. From the project directory, run:

   ```bash
   docker compose up --build -d
   ```
3. Test the endpoints in a browser:
   - `http://localhost:8000/` → greeting JSON
   - `http://localhost:8000/db` → `{"status":"connected","database":"MongoDB"}` when the connection works
   - `http://localhost:8000/docs` → interactive FastAPI API documentation
4. View logs with `docker compose logs -f`.
5. Stop containers with `docker compose down`.

> `docker compose down -v` also removes the MongoDB volume and its stored data. Use it only when you intend to reset the database.

## Files

- `Dockerfile`: builds the FastAPI image
- `docker-compose.yaml`: runs and networks both services
- `app/main.py`: defines HTTP endpoints and checks MongoDB connectivity
- `requirements.txt`: Python dependencies
- `.env.example`: example local configuration; `.env` stays untracked

## Skills demonstrated

Docker, Docker Compose, container networking, FastAPI, MongoDB connectivity, and local environment configuration.

## Scope

This is a containerization and service-integration demo, **not** an ETL/data pipeline. The `/db` endpoint verifies connectivity; it does not perform data ingestion or analytics.
