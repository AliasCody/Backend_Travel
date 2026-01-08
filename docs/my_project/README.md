# DRF Backend MVP

> A production-oriented backend MVP built with Django REST Framework.

---

## Table
* [1. Overview](#overview)
* [2. Project Goals](#project-goals)
* [3. Development Plan](#development-plan)
* [4. Tech Stack](#tech-stack)
* [5. Core Features](#core-feature)
* [6. API Design](#api-design)
* [7. Testing Strategy](#testing-strategy)
* [8. API Documentation](#api-documentation)
* [9. Deployment](#deployment)
* [10. ProjectHilights](#projecthilights)
* [11. Motivation](#motivation)
* [12. Notes & Future Improvements](#notes--future-improvements)
* [13. License](#license)



## Overview

This project is a **backend MVP** designed and implemented using a **time-boxed sprint approach**.  
The goal is to build a **production-ready RESTful API** within **60 hours**, covering not only core features but also testing, documentation, and deployment readiness.


---

## Project Goals

- Build a RESTful API with **user authentication**
- Implement a **single core resource CRUD**
- Apply **permission and ownership control**
- Write **unit tests** for critical endpoints
- Generate **API documentation**
- Prepare the project for **cloud deployment**

> Focus: *Delivering a realistic MVP, not a demo.*

---

## Development Plan

The project follows a **4-week sprint plan**, with clearly defined deliverables for each stage.

| Week | Focus |
|-----|------|
| Week 1 | Project setup & user authentication |
| Week 2 | Core resource CRUD & permissions |
| Week 3 | Testing & business logic |
| Week 4 | Documentation & deployment preparation |

Detailed sprint breakdown can be found in:  
`docs/sprint-plan.md`

---

## Tech Stack

**Backend**
- Python
- Django
- Django REST Framework

**Authentication**
- JWT (access & refresh tokens)

**Database**
- PostgreSQL (production-ready setup)

**Testing**
- Django Test Client
- Pytest *(optional / expandable)*

**Documentation**
- drf-spectacular (OpenAPI / Swagger)

**Deployment**
- Gunicorn
- Render.com *(or equivalent PaaS)*

---

## Core Features

- User registration & login
- JWT-based authentication
- Core resource CRUD (e.g. Todo)
- Ownership-based access control
- Business logic handling (e.g. auto `completed_at`)
- Unit tests for auth and CRUD APIs
- Auto-generated API documentation

> Additional features may be added incrementally.

---

## API Design

> _This section will be expanded as the project evolves._

Planned API structure follows RESTful conventions and emphasizes:
- Clear resource boundaries
- Predictable HTTP status codes
- Serializer-level validation

Future documentation:
- Endpoint list
- Request / response examples
- Error handling strategy

---

## Testing Strategy

> _Details to be expanded._

Testing focuses on:
- Authentication flows
- Core CRUD operations
- Permission enforcement
- Business logic validation

The goal is to ensure **confidence in refactoring and deployment**.

---

## API Documentation

Swagger / OpenAPI documentation is generated using **drf-spectacular**.

> _Link or screenshots will be added after setup._

---

## Deployment

> _Deployment details will be finalized in later stages._

The project is prepared for deployment with:
- Environment variable management
- Production-ready settings
- WSGI server configuration

Target platform:
- Render.com *(or similar PaaS)*

---

## Project Highlights

- Designed with **MVP mindset**
- Time-boxed development (60 hours)
- Emphasis on **code quality & maintainability**
- Includes testing and documentation from early stages
- Structured for real-world backend workflows

---

## Motivation

This project was created to simulate a **real backend engineering workflow**, from planning to delivery, rather than focusing on isolated features.

It serves as a **technical showcase** and a **discussion piece for interviews**.

---

## Notes & Future Improvements

> _Reserved space for future iterations._

- Additional business rules
- Advanced filtering & pagination
- Security enhancements
- Performance optimizations
- CI/CD integration

---

## License

This project is intended for educational and portfolio purposes.
