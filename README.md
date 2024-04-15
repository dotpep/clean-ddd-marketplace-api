# Clean DDD Architected Django Boilerplace (Marketplace)

This is ideal, clean and well-structured/architected Django Boilerplate and example using Django, Django Ninja, Postgres, Docker and Makefile

## Demonstration

### Django Ninja Swagger Docs of API endpoints

![API Swagger Docs](docs/assets/api_endpoints.png)

## Tech Stack

- Docker
- Makefile
- Django Ninja for REST API like FastAPI with Pydantic
- PostgreSQL
- Poetry

## TO DO

- [x] Docker Compose for separated PostgreSQL and Main-App with `.env` file
- [x] Implement Makefile commands to iteraction with Docker Compose
- [ ] Implement DDD architecture, Clean Architecture with applying Clean Code, SOLID principles and Patterns
    - [ ] Write docstring for class
    - [x] Implement Simple DDD Architecture with layer (Domain, Services, DTO) most like Onion Architecture
    - [x] Apply Dependency Injection for api endpoints handlers and services and Composite Pattern
- [x] Setup Linters/Formatter and Pre-commit
- [x] Write Tests using Pytest
- [ ] Authentication and Authorization with JWT Token
    - [ ] Implement Custom Exceptions for Auth Service
    - [ ] Implement Redis Cache CodeService
- [ ] Elasticsearch APM and Kibana (ELK) logging and monitoring system

## Features

- Simple DDD Architecture with layers for Business Logic and Process
- Applied SOLID Principles and OOP Patterns
- Dependency Injection container to resolve dependencies and using Base Interface classes
- Linters/Formatter and Pre-commit
- Database and Project in Docker compose and makefile to run commands in one command
- OpenAPI Docs
- Writed Unit Tests

## Architecture

Layers

1. API (endpoint handlers)
2. Domain (Entity)
3. Services
4. UseCases
5. DTO + Repo in Service layer
6. Others

---
Notes:

- Entity is Domain Business logic Interface and Base Class or Abstract Class
- Both Service and Repository layers implemented in Service layer
- UseCases Business Process using Services (services uses repository to get data)
- DTO (Data Transfer Object) and Repo interacts only with data

Entity is like core,
Service must provide atomicity, UseCase uses Services to process something,
Repository communicate with services and only interact with data,
Task queue broker and Web handler communicate with Use Cases and external world,
Client, Providers and Repositories communicate with Service and external world,

---

## Requirements

- [Python](https://www.python.org/downloads/)
- [Poetry(Optional)](https://python-poetry.org/docs/#installation)
- [Docker](https://docs.docker.com/get-docker/)
- [GNU Make](https://www.gnu.org/software/make/#download) (install on windows using chocolatey package manager)

## How to Use

1. **Clone this repository**

```bash
git clone https://github.com/dotpep/clean-ddd-marketplace-api.git
cd clean-marketplace
```

2. Install all dependencies and required packages
3. Change `.env.example` file to `.env` with provided your environment variables

## Implemented Makefile Commands

### Docker specific commands

- `make app` - up django server container
- `make app-logs` - display logs of django server
- `make app-down` - down django server container
- `make storages` - up storages in separated container (then you can run django server locally)
- `make storages-logs` - display storages logs
- `make storages-down` - down storage container

---

- `make postgres` - enter to postgres db interactive shell mode (psql) to perform SQL queries
- `make postgres-db` - immediately go to project database interactive shell mode
- `make ash` - enter to interactive ash shell of project app for alpine docker image
- `make django-shell` - enter to django shell of project app using ipython interactive mode

### Django specific commands

- `make migrations` - make migrations on models
- `make migrate` - apply all migrations
- `make superuser` - create admin user
- `make collectstatic` - collect all static files in project to base-dir static folder

---

- `make run-tests` - run django integrated database tests (requires `make app`, run django server)
