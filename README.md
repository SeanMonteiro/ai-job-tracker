# AI Job Tracker

AI Job Tracker is a backend API built with FastAPI to help users track job applications and generate AI-powered job analysis from job descriptions.

The project demonstrates production-style backend development using layered architecture, PostgreSQL persistence, JWT authentication, AI service integration, structured logging, database migrations, and deployment-ready API design.


## Project Overview
AI Job Tracker allows authenticated users to:
- Register and log in securely
- Create structured job applications and raw job description from text
- Generate AI-powered job analysis using OpenAI
- Store job and AI analysis results in PostgreSQL
- Retry AI analysis for existing jobs
- Preserve versioned AI analysis records per job
- Update and delete jobs with ownership enforcement
- Test the API through Swagger UI and Postman collections

## Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Pydantic
- Python 3.11
- Alembic (Database Migrations)
- JWT Authentication
- Passlib (Password Hashing)
- Python-Jose (JWT Handling)
- OpenAI API
- Python Logging
- Postman for manual API testing


## Architecture and Backend Features
- Service Layer architecture
- Repository Pattern implementation
- Dependency Injection for services / repositories
- Clean layered backend structure
- Structured logging with request correlation (Request ID middleware)
- Centralized exception handling using an AppException system
- Domain-driven HTTP exception mapping
- JWT authentication and authorization layer
- Password hashing and credential verification
- Multi-user ownership enforcement for protected resources
- Route-level authentication using FastAPI dependency injection
- Rotating file log management
- Standardized API response contract (success/data/message structure)
- Fault-Tolerant AI analysis design
- Input size validation for AI endpoints
- Versioned AI analysis records
- AI retry analysis workflow
- AI failure simulation support for local testing

## API Features

### Authentication 
- User registration and login
- JWT- token generation
- Protected authenticated routes
- Current user endpoint

### Job Management
- Create, Update and Delete jobs
- List authenticated user jobs
- Fetch job by ID with ownership validation
- Prevent unauthorized cross-user job access

### AI Analysis
- Create job with AI analysis from structured JSON
- Create job with AI analysis from raw text input
- Parse raw job text into structure job fields
- Generate AI-powered analysis using OpenAI
- Store AI analysis separately from job data
- Track analysis version per job
- Retry AI analysis for existing jobs
- Preserve previous AI analysis versions
- Gracefully handle AI failures without blocking job creation

### Health and Diagnostics
- Service and Database health endpoint
- Debug AI failure toggle for local testing

## Database & Migration System
- Alembic configured for schema versioning
- Version-controlled database schema history
- PostgreSQL relational schema
- User-to-Job ownership relationship
- Job-to-Job analysis relationship
- Foreign key constraints for multi-user data isolation
- Cascade delete behavior for related job analysis records
- Upgrade / Downgrade support for schema changes

## Engineering Practices
- Incremental feature branching workflow
- Production style backend refactoring approach
- Database migration strategy (schema versioning instead of manual SQL)
- Clean separation of concerns across routes, services, repositories and AI components
- Stateless authentication architecture using JWT
- Ownership-based authorization enforcement
- Centralized logging and exception handling
- Manual sanity testing through Postman
- API validation using Pydantic schemas
- Deployment-oriented project structure

## API Testing
The API can be tested using: 
- Swagger UI/ OpenAPI docs
- Included Postman collection

The Postman collection covers:
- Health checks
- Authentication flow
- Job CRUD operations
- AI analysis workflows
- Retry Analysis
- Ownership validation
- Schema validation scenarios
- AI failure simulation
- Cleanup requests

Local Swagger UI:
http://localhost:8000/docs

## Future Improvements
- Refresh token system
- Resume-to-job match scoring
- AI generated application insights
- Redis cache layer
- Docker containerization
- CI/CD Pipeline
- Frontend dashboard
- Rate limiting for AI endpoints
- Automated integration tests using pytest and/or Newman