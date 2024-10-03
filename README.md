# TODO Application

This is a simple TODO application built with FastAPI, SQLAlchemy, and JWT authentication.

## Features
- User registration and login.
- Create, read, update, and delete TODO tasks.
- JWT-based authentication.

## Setup

1. Clone the repository.
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application:
    ```bash
    uvicorn main:app --reload
    ```
4. Navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation.

## Running Tests
To run the tests:
```bash
pytest
