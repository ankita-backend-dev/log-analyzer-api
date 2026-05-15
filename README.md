# Log Analyzer API

A FastAPI-based backend application that analyzes application log files and provides categorized summaries of log data.

## Features

- Upload `.log` files
- Analyze INFO, WARNING, and ERROR logs
- Extract error and warning entries
- REST API using FastAPI
- Swagger API documentation
- Modular project structure

## Tech Stack

- Python
- FastAPI
- Uvicorn

## Project Structure

```plaintext
app/
├── main.py
├── routes/
├── services/
└── utils/