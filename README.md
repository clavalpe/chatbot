# Chatbot

## Table of Contents

- [Overview](#overview)
- [Usage](#usage)
  - [Swagger Documentation](#swagger-documentation)
  - [Endpoint](#endpoint)
  - [Example Usage with cURL](#example-usage-with-curl)
- [Installation](#installation)
  - [Deploying with Uvicorn](#deploying-with-uvicorn)
  - [Deploying with Docker](#deploying-with-docker)
  - [Build and start the application using Docker Compose](#build-and-start-the-application-using-docker-compose)

## Overview

The Chatbot application is a RESTful API designed to facilitate natural language interactions with users. It leverages the OpenAI GPT model to process user inputs and generate contextual responses. The application is built to be lightweight, scalable, and easily deployable, supporting both Docker and Docker Compose setups.

Key features include:

- **Interactive Chat Endpoint**: A POST endpoint for real-time conversations with the chatbot.
- **Health Check Endpoint**: A GET endpoint to monitor application health.
- **Swagger Integration**: Interactive API documentation to test and explore endpoints.
- **Easy Deployment**: Dockerized setup for seamless installation and deployment.


## Usage

### Swagger documentation
You can access the interactive chatbot API documentation via Swagger at the following URL: 

  - Swagger UI Documentation [http://localhost:8000/swagger](http://localhost:8000/swagger)


### Endpoints
The application provides several endpoints, including the health check and chatbot interaction. 

- **GET** `http://localhost:8000/health/`  
  Verifies the status and health of the application.

- **POST** `http://localhost:8000/chat/`  
  Allows interaction with the chatbot. 

### Example usage with cURL
To check the health status of the chatbot, use the following `curl` command:

```bash
curl --request GET 'http://localhost:8000/health/' 
```

To send a message to the chatbot, use the following curl command. Replace the <message> placeholder with the message you want to send:

```bash
curl --request POST 'http://localhost:8000/chat/' \
--header 'Content-Type: application/json' \
--data '{"user": "Hi, can you help me with something?"}'
```

## Installation
Follow the instructions below to install and deploy the chatbot application.

**Set OpenAI API key**
* If you don't have an OpenAI API key, you can sign up [here](https://openai.com/index/openai-api/).
*  Set `OPENAI_API_KEY` in your environment


**Clone the repository:**

    ```bash
    git clone https://github.com/clavalpe/chatbot
    cd chatbot
    ```


### Deploying with Uvicorn
To run the application locally using Uvicorn, follow these steps:

1. **Set environment variables:**

    Before running the application, set up the .env file in the root directory. This file should contain the OPENAI_API_KEY variable and any other required environment variables. Here's an example:

    ```bash
    echo "OPENAI_API_KEY=<your_openai_api_key>" > .env
    ```

2. **Install dependencies:**

    Ensure you have Python and pip installed. Then, install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application:**

    Use the following command to start the application with Uvicorn:

    ```bash
    uvicorn src.main:app --reload
    ```

    This command will start the application in development mode with hot-reloading enabled. The application will be available at [http://localhost:8000](http://localhost:8000).

4. **Verify the application:**

    - Access the Swagger documentation at [http://localhost:8000/swagger](http://localhost:8000/swagger).
    - Check the health endpoint by navigating to [http://localhost:8000/health/](http://localhost:8000/health/).


### Deploying with Docker
To deploy the chatbot application using Docker, follow these steps:

1. **Build the Docker image:**

    ```bash
    docker build -t chatbot .
    ```

2. **Run the Docker container:**

    ```bash
    docker run --name mychatbot -p 8000:8000 -e OPENAI_API_KEY=<replace_with_your_key> chatbot
    ```

    This command will start the application on port 8000. You can access the application at [http://localhost:8000](http://localhost:8000).

### Docker Compose

Run the following command to build and start the chatbot service:

*  Set `OPENAI_API_KEY` in docker-compose.yml file 

** Build and start the application **

```bash
docker-compose up --build -d
```

This command will:
- Build the Docker image if it hasn't been built already.
- Start the application container in detached mode (`-d`).

**Stopping the application:**

To stop the application, run:

```bash
docker-compose down
```

This will stop and remove the container.