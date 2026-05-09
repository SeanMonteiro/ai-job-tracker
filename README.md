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
- JWT Authentication
- Passlib (Password Hashing)
- Python-Jose (JWT Handling)

## Architecture and Backend Features
- Service Layer architecture
- Repository Pattern implementation
- Dependency Injection for services / repositories
- Structured logging with request correlation (Request ID middleware)
- Centralized exception handling (AppException-based system)
- Domain-driven HTTP exception mapping
- JWT authentication and authorization layer
- Password hashing and credential verification
- Multi-user ownership enforcement for protected resources
- Route-level authentication using FastAPI dependency injection
- Rotating file log management
- Clean layered backend structure
- Database migration system using Alembic
- Model-driven schema generation using SQLAlchemy metadata + Alembic Autogenerate
- Standardized API response contract (success/data/message structure)

## API Features
- User registration and login
- JWT-based authentication
- Create jobs
- Update jobs
- Delete jobs
- List authenticated user jobs
- Fetch job by ID with ownership validation
- Protected API routes
- REST API with Swagger UI
- Response Validation using Pydantic Schemas

## Database & Migration System
- Alembic configured for schema versioning
- Initial migration for 'jobs' table
- Upgrade / Downgrade support for schema changes
- Version-controlled database schema history
- User-to-job relational ownership mapping
- Foreign key constraints for multi-user data isolation

## Engineering Practices
- Incremental feature branching workflow
- Production style backend refactoring approach
- Database migration strategy (schema versioning instead of manual SQL)
- Clean separation of concerns across layers
- Stateless authentication architecture using JWT
- Ownership-based authorization enforcement
- Layered authentication and authorization separation

## Upcoming
- Phase 5 AI differentiation layer
