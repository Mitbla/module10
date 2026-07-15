# Reflection

## What I built
I implemented a secure FastAPI user model with SQLAlchemy, Pydantic validation, password hashing, and database-backed tests. I also added a CI/CD workflow that runs tests in GitHub Actions, scans the Docker image, and pushes the image to Docker Hub after a successful main-branch build.

## Challenges
The most important challenge was keeping the application secure while still making the code simple enough for an assignment submission. I had to make sure plaintext passwords are never stored, validation happens before the database layer, and the integration tests use a real database so unique constraints behave correctly.

## What I learned
This project reinforced how Pydantic and SQLAlchemy work together in FastAPI, how to structure unit and integration tests, and how GitHub Actions can automate both verification and deployment. It also showed the value of using a containerized Postgres service in CI for realistic database testing.

## Next steps
If this were extended into a final project, I would add authentication endpoints, JWT-based login, password reset support, and a migration tool such as Alembic.
