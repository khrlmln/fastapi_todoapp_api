# FastAPI Todo API

This is a simple Todo API built using FastAPI. It includes user authentication, role-based access control, and CRUD operations for managing todos. The application uses PostgreSQL as the database and provides a RESTful API for interacting with the system.

## Features

- **User Authentication**: Secure user authentication using hashed passwords and JWT tokens.
- **Role-Based Access Control**: Admin users can manage all todos, while regular users can only manage their own todos.
- **CRUD Operations**: Create, read, update, and delete todos.

## Setup and Installation

### Prerequisites

- Python 3.13 or higher
- PostgreSQL

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/khrlmln/fastapi_todoapp_api.git
   cd fastapi_todoapp_api
   ```

2. Install dependencies using `uv`:

   ```bash
   uv sync
   ```

3. Start the application:

   ```bash
   uv run uvicorn main:app --reload
   ```

4. Access the API at `http://127.0.0.1:8000`.
