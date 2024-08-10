# Book Management REST API

## Overview

The **Book Management REST API** is a backend service that provides a set of endpoints to manage books in a library system. This API allows for operations such as creating, reading, updating, and deleting book records.

## Features

- **CRUD Operations**: Create, read, update, and delete book entries.
- **Search and Filter**: Search books by title, author, or genre.
- **Authentication**: Secure endpoints with authentication mechanisms (if applicable).
- ** Swagger API ** : Swagger API end point where API's are documented how to use 

## Installation

You can run the project using either environment variables or Docker. Follow the instructions for the method you prefer.

### Running with Environment Variables

1. **Clone the Repository**

   ```bash
   git clone https://github.com/sathwik04/Bookmanagement_RestAPI.git
   cd Bookmanagement_RestAPI

Running with Docker
Ensure Docker is Installed

Follow the instructions on the Docker website to install Docker on your system.
Build the Docker Image

bash
Copy code
docker build -t bookmanagement-api .
Run the Docker Container

bash
Copy code

docker run -d -p 8000:8000 bookmanagement-api


Ensure you have a .env file in the root directory with the necessary environment variables as described in the Environment Variables section.

API Endpoints
Books
GET /api/books: Retrieve a list of all books.

POST /api/books: Add a new book.

GET /api/books/
: Retrieve a book by its ID.
PUT /api/books/
: Update a book by its ID.

DELETE /api/books/
: Delete a book by its ID.

Authentication (if applicable)
POST /api/auth/login: Log in and receive a token.
POST /api/auth/register: Register a new user.
