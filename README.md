# Laboratory Assignments for "Programming, Databases, and Knowledge Bases" Course

## Overview
This repository contains materials for the laboratory assignments of the course **"Programming, Databases, and Knowledge Bases"**, taught at the National Technical University "Kharkiv Polytechnic Institute". The course is designed for students of the 122 specialty "Computer Science".

The repository provides Dockerized skeletons for each lab assignment. Students are expected to use these skeletons as a foundation to implement the required functionality according to their specific subject area variants.

## Repository Structure

```bash
.
├── docker/                     # Basic Docker examples (for lecture assist)
├── L14.security/               # Materials for security-related topics (for lecture assist)
├── lab2_docker_sample/         # Skeleton for Lab 2: Logical Database Design
├── lab3_docker_sample/         # Skeleton for Lab 3: Database Interaction with ORM
├── lab3_docker_sample_mysql/   # Variant of Lab 3 with MySQL support
├── lab4_docker_sample/         # Skeleton for Lab 4: Data Caching and Stored Procedures
├── lab5_app/                   # Skeleton for Lab 5: Application Development with RESTful APIs
├── todo/                       # Additional tasks or notes for the course
└── README.md                   # This documentation file
```

## Laboratory Assignments

### Lab 1: Infological Design of Databases

**Objective:** Learn the basics of database infological design by creating an Entity-Relationship (ER) model.

**Key Tasks:**
- Identify entities, attributes, and relationships.
- Create an ER diagram using tools like [draw.io](https://app.diagrams.net/) or [dbdiagram.io](https://dbdiagram.io/).
- Document the infological design in a detailed report.

---

### Lab 2: Logical Database Design

**Objective:** Perform logical design for a relational database and implement the schema using an RDBMS.

**Key Tasks:**
- Normalize relations up to the 3rd Normal Form (3NF).
- Design and create the relational schema.
- Implement the schema and populate the tables in PostgreSQL using the provided Docker skeleton.
- Write SQL queries for data manipulation and retrieval (INSERT, UPDATE, SELECT, DELETE).

---

### Lab 3: Interaction with Databases using ORM

**Objective:** Learn to interact with databases using Object-Relational Mapping (ORM).

**Key Tasks:**
- Define data models and relationships in Python using an ORM (e.g., SQLAlchemy).
- Perform CRUD operations (Create, Read, Update, Delete) using ORM methods.
- Execute advanced queries and filters using ORM.
- **MySQL Variant:** Use the `lab3_docker_sample_mysql` folder to implement the same functionality with MySQL.

---

### Lab 4: Data Caching and Stored Procedures

**Objective:** Implement data caching mechanisms and utilize stored procedures and triggers for advanced database functionalities.

**Key Tasks:**
- Configure and use Memcached for data caching.
- Create triggers to keep cached data synchronized with database changes.
- Write stored procedures for complex database operations.
- Integrate the caching mechanism with the application using the Dockerized setup.

---

### Lab 5: RESTful API Development

**Objective:** Build a RESTful API to interact with a relational database.

**Key Tasks:**
- Design and develop RESTful endpoints for CRUD operations.
- Use frameworks like Flask or FastAPI in Python.
- Implement authentication for API endpoints.
- Connect the API with the database and test functionality in the Docker environment.
