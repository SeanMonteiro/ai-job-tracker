# AI Job Tracker

Backend API built with FastAPI to track and manage job applications.

## Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Pydantic
- Python 3.11 (WSL)
- Dependency Injection (FastAPI Depends)
- Alembic (Database Migrations)

## Architecture and Backend Features
- Service Layer architecture
- Repository Pattern implementation
- Dependency Injection for services / repositories
- Structured logging with request correlation (Request ID middleware)
- Centralized exceptions handling (AppException based system)
- Structured HTTP over mapping via domain exceptions
- Rotating file log management
- Clean layered backend structure
- Database migration system using Alembic
- Model-driven schema generation using SQLAlchemy metadata + Alembic Autogenerate
- Standardized API response contract (success/data/message structure)

## API Features
- Create jobs
- List jobs
- Fetch job by ID
- REST API with Swagger UI
- Response Validation using Pydantic Schemas

## Database & Migration System
- Alembic configured for schema versioning
- Initial migration for 'jobs' table
- Upgrade / Downgrade support for schema changes
- Version-controlled database schema history

## Engineering Practices
- Incremental feature branching workflow
- Production style backend refactoring approach
- Database migration strategy (schema versioning instead of manual SQL)
- Clean separation of concerns across layers

## Upcoming
- User Accounts
- Login System (JWT)
- Protected routes
- User-specific job tracking
- Basic security layer
