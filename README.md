# AI Job Tracker

Backend API built with FastAPI to track and manage job applications.

## Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Pydantic
- Python 3.11 (WSL)
- Dependency Injection (FastAPI Depends)

## Architecture and BackEnd Features
- Service Layer architecture
- Repository Pattern implementation
- Dependency Injection for services/ repositories
- Structured logging system
- Request Correlation middlewar (Request ID tracking)
- Global exception handling
- Custom Application exceptions
- Rotating file log management
- Clean layered backend structure

## API Features
- Create jobs
- List jobs
- Fetch job by ID
- REST API with Swagger UI
- Response Validation using Pydantic Schemas

## Engineering Practices
- Incremental feature branching workflow
- Production style backend refactoring approach

## Upcoming
- Alembic database migration suppprt (Phase 3 in progress)
