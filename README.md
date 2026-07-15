# Module 10: Secure User Model, Validation, Testing, and Docker Deployment

This project is a FastAPI application that demonstrates a secure SQLAlchemy user model, Pydantic validation, password hashing, database-backed testing, and a Docker/GitHub Actions deployment pipeline.

## Features
- SQLAlchemy `User` model with unique `username` and `email`
- `created_at` timestamp
- Pydantic `UserCreate` and `UserRead` schemas
- Password hashing and verification with Passlib
- Unit tests for hashing and schema validation
- Integration tests against a real database
- Docker image build and push workflow

## Run locally
1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -e .[test]
   ```
3. Run tests:
   ```bash
   pytest
   ```
4. Start the API:
   ```bash
   uvicorn app.main:app --reload
   ```

## Environment variables
- `DATABASE_URL` - database connection string

Example:
```bash
export DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/module10_test
```

## Docker
Build the image locally:
```bash
docker build -t module10-secure-user-model .
```
Run the image:
```bash
docker run -p 8000:8000 module10-secure-user-model
```

## Docker Hub
Replace the placeholder below with your own Docker Hub repository link.

- Docker Hub repository: https://hub.docker.com/r/mitbla/module10-secure-user-model
- Docker image: `mitbla/module10-secure-user-model:latest`

## GitHub Actions
The workflow in `.github/workflows/ci-cd.yml` runs tests with a Postgres service, scans the Docker image, and pushes the image to Docker Hub when changes land on `main`.
