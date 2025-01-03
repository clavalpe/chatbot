# Chatbot

## Table of Contents

- [Overview](#overview)
- [Usage](#usage)
  - [Endpoint](#endpoint)
  - [Example Usage with cURL](#example-usage-with-curl)
  - [Response](#response)
- [Installation](#installation)
  - [Deploying with Docker](#deploying-with-docker)
  - [Build and start the application using Docker Compose](#build-and-start-the-application-using-docker-compose)

## Overview

## Usage

### Endpoint
The application provides an endpoint to verify its status and health. 

- **GET** `http://localhost:8000/health/`

### Example usage with cURL
To check the health status of the chatbot, use the following `curl` command:

```bash
curl --request GET 'http://localhost:8000/health/' 
```

### Response
```json
{
    "status": "healthy"
}
```

## Installation
Follow the instructions below to install and deploy the chatbot application.

### Deploying with Docker
To deploy the chatbot application using Docker, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/clavalpe/chatbot
    cd chatbot
    ```

2. **Build the Docker image:**

    ```bash
    docker build -t chatbot .
    ```

3. **Run the Docker container:**

    ```bash
    docker run -d -p 8000:8000 chatbot
    ```

    This command will start the application on port 8000. You can access the application at [http://localhost:8000](http://localhost:8000).

### Build and start the application using Docker Compose

Run the following command to build and start the chatbot service:

```bash
docker-compose up --build -d
```

This command will:
- Build the Docker image if it hasn't been built already.
- Start the application container in detached mode (`-d`).
- Map port 8000 on your local machine to port 8000 in the container.

**Stopping the application:**

To stop the application, run:

```bash
docker-compose down
```

This will stop and remove the container.