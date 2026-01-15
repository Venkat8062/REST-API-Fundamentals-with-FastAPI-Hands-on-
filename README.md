# REST API Fundamentals with FastAPI (Hands-on)

## Overview

This repository contains a **simple, stateless REST API** built using **FastAPI**.  
The project is designed as a **hands-on learning lab** to understand:

- What a REST API is
- How request–response flow works
- How APIs are hosted locally
- How backend services are structured before containerization

The application implements a **calculator API** with health and readiness endpoints, following patterns commonly used in real-world backend and cloud-native systems.

---

## Tech Stack

- **Python 3.12**
- **FastAPI** – REST API framework
- **Uvicorn** – ASGI web server
- **Pydantic** – Request validation

---

## Project Structure

```text
calculator-api/
├── main.py           # Application code and API endpoints
├── requirements.txt  # Python dependencies
├── .gitignore        # Git ignore rules
└── README.md         # Project documentation
```
## API Endpoints

### Health Check
**GET** `/health`

Used to verify that the application is running.

**Response**
```json
{
  "status": "ok"
}

### Calculator
**POST** `/calculate`

Performs a calculation based on the input.

#### Request Body
```json
{
  "a": 10,
  "b": 5,
  "operation": "add"
}

#### Supported Operations
- `add`
- `subtract`
- `multiply`
- `divide`

#### Response
```json
{
  "a": 10,
  "b": 5,
  "operation": "add",
  "result": 15
}
```

Running the Application Locally

    Create and Activate Virtual Environment python3 -m venv venv source venv/bin/activate

    Install Dependencies pip install -r requirements.txt

    Run the Application uvicorn main:app --reload

The API will be available at:

http://127.0.0.1:8000

API Documentation (Swagger UI)

FastAPI automatically generates interactive API documentation.

Access it here:

http://127.0.0.1:8000/docs

Key Learnings

Built a stateless REST API

Understood request–response flow

Used FastAPI for routing and validation

Used Uvicorn to run a local HTTP server

Followed clean project and Git practices

Next Steps

This repository will be extended step by step to cover:

Dockerizing the application

Running the API in Kubernetes (Minikube)

CI/CD using Jenkins

Infrastructure automation concepts

This marks the completion of the local REST API phase.

Author

Venkatraman Hands-on DevOps & Cloud Learning Project
Calculator

POST /calculate

Performs a calculation based on the input.

Request Body

{
  "a": 10,
  "b": 5,
  "operation": "add"
}


Supported Operations

add

subtract

multiply

divide

Response

{
  "a": 10,
  "b": 5,
  "operation": "add",
  "result": 15
}

Running the Application Locally
1. Create and Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate

2. Install Dependencies
pip install -r requirements.txt

3. Run the Application
uvicorn main:app --reload


The API will be available at:

http://127.0.0.1:8000

API Documentation (Swagger UI)

FastAPI automatically generates interactive API documentation.

Access it here:

http://127.0.0.1:8000/docs

Key Learnings

Built a stateless REST API

Understood request–response flow

Used FastAPI for routing and validation

Used Uvicorn to run a local HTTP server

Followed clean project and Git practices

Next Steps

This repository will be extended step by step to cover:

Dockerizing the application

Running the API in Kubernetes (Minikube)

CI/CD using Jenkins

Infrastructure automation concepts

This marks the completion of the local REST API phase.

Author

Venkatraman
Hands-on DevOps & Cloud Learning Project
