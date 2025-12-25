# FastAPI CRUD Demo

A comprehensive FastAPI application demonstrating CRUD (Create, Read, Update, Delete) operations with authentication, database integration, and API versioning.

## Features

- **FastAPI Framework**: Modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **SQLModel Integration**: Uses SQLModel for database modeling and operations with SQLAlchemy and Pydantic.
- **Authentication System**: JWT-based authentication with access and refresh tokens.
- **CRUD Operations**: Complete CRUD functionality for users and articles with pagination support.
- **Database Support**: SQLite database with async support using aiosqlite driver.
- **API Versioning**: API endpoints versioned under `/api/v1`.
- **CORS Support**: Configurable Cross-Origin Resource Sharing.
- **Response Formatting**: Standardized response format for consistent API responses.
- **Environment Configuration**: Flexible configuration through environment variables.

## Tech Stack

- Python 3.12+
- FastAPI
- SQLModel
- SQLAlchemy
- Pydantic
- JWT for authentication
- Bcrypt for password hashing
- Alembic for database migrations
- Uvicorn ASGI server

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd fastapi-curd-demo
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -e .
   ```

4. Set up environment variables by copying the example:

   ```bash
   cp .env.example .env
   ```

5. Configure your environment variables in the `.env` file (see Configuration section below).

6. Run database migrations:
   ```bash
   alembic upgrade head
   ```

## Configuration

The application uses environment variables for configuration. The following variables can be set in your `.env` file:

### Application Settings

- `APP_PORT`: Port number for the application (default: 8000)
- `APP_DEBUG`: Enable debug mode (true/false, default: false)
- `APP_CORS`: Enable CORS (true/false, default: true)

### JWT Settings

- `ACCESS_TOKEN_EXPIRE_TIME`: Access token expiration time in seconds (default: 30 seconds)
- `REFRESH_TOKEN_EXPIRE_TIME`: Refresh token expiration time in seconds (default: 604800 seconds = 7 days)
- `ACCESS_TOKEN_SECRET`: Secret key for access tokens (default: d3157a5812d456910c9b26a1647963bf)
- `REFRESH_TOKEN_SECRET`: Secret key for refresh tokens (default: ed71580c1d2f1d7c5c49278f20e136c5)

### Database Settings

- `DB_URL`: Database URL (default: "sqlite+aiosqlite:///database.db")

## Database Models

### User Model

- `id`: Primary key (int)
- `username`: User's username (string, max 32 chars)
- `email`: User's email (string, max 128 chars, required)
- `telephone`: User's phone number (string, max 16 chars, optional)
- `password`: Hashed password (string, max 128 chars, required)
- `avatar_url`: User's avatar URL (string, max 256 chars, optional)
- `created_at`: Creation timestamp (string)
- `updated_at`: Update timestamp (string, optional)

### Article Model

- `id`: Primary key (int)
- `author_id`: Foreign key to users table (int, required)
- `title`: Article title (string, max 128 chars, required)
- `content`: Article content (string, max 128 chars, required)
- `like_count`: Number of likes (int, default: 0)
- `star_count`: Number of stars (int, default: 0)
- `share_count`: Number of shares (int, default: 0)
- `visit_count`: Number of visits (int, default: 0)
- `comment_count`: Number of comments (int, default: 0)
- `created_at`: Creation timestamp (string)
- `updated_at`: Update timestamp (string, optional)
- `deleted_at`: Deletion timestamp (string, optional, for soft deletes)

## API Endpoints

All API endpoints are prefixed with `/api/v1`.

### Public Endpoints (No Authentication Required)

#### Authentication

- `POST /api/v1/register` - Register a new user

  ```json
  {
    "account": "user@example.com",
    "password": "md5_hashed_password"
  }
  ```

- `POST /api/v1/login` - Login and get JWT tokens

  ```json
  {
    "account": "user@example.com",
    "password": "md5_hashed_password"
  }
  ```

  Returns: User info with `accessToken` and `refreshToken`

- `GET /api/v1/refresh_access_token?refreshToken={refreshToken}` - Refresh access token using refresh token

### Protected Endpoints (Authentication Required)

#### Articles

- `GET /api/v1/articles?page={page}&limit={limit}` - List articles with pagination
- `POST /api/v1/articles` - Create a new article
  ```json
  {
    "author_id": 1,
    "title": "Sample Article",
    "content": "Article content here..."
  }
  ```
- `PATCH /api/v1/articles/{id}` - Update an article
  ```json
  {
    "title": "Updated Title"
  }
  ```
- `DELETE /api/v1/articles/{id}` - Delete an article (soft delete)

#### General

- `GET /` - Health check endpoint (returns "server is running")

## Authentication

The application uses JWT (JSON Web Tokens) for authentication:

- Access tokens expire after a configurable time (default: 30 seconds)
- Refresh tokens expire after a longer period (default: 7 days)
- All protected endpoints require a valid access token in the Authorization header: `Authorization: Bearer {accessToken}`
- When access token expires, use the refresh token endpoint to get a new access token

## Running the Application

### Development

```bash
python main.py
```

or

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Seeding Data

To seed sample data into the database:

```bash
python seeder.py
```

This will create 5 sample users and 50 sample articles.

## Response Format

All API responses follow a consistent format:

```json
{
  "success": true,
  "message": "success",
  "data": { ... }
}
```

For errors:

```json
{
  "success": false,
  "message": "error message",
  "data": null
}
```

## Pagination

List endpoints support pagination with the following parameters:

- `page`: Page number (default: 1, minimum: 1)
- `limit`: Items per page (default: 10, minimum: 10, maximum: 50)

## Error Handling

The application handles various error scenarios:

- Unauthorized access (401)
- Resource not found (404)
- Bad requests (400)
- Internal server errors (500)

## Database Migrations

The application uses Alembic for database migrations:

- To create a new migration: `alembic revision --autogenerate -m "description"`
- To apply migrations: `alembic upgrade head`
- To downgrade: `alembic downgrade <revision>`
