# BFHL Python Qualifier - Webhook & SQL Automation

This project was created as a solution for the Bajaj Finserv Health - PYTHON Qualifier Round 1.

## Problem Overview

Upon running the application:
- It sends a POST request to generate a webhook URL and an access token.
- It solves a given SQL problem based on employee salary records.
- It submits the final SQL query to the generated webhook endpoint using authorization.

No manual user input is needed after startup — the entire flow is automated.

## Tech Stack
- Python 3
- Requests Library (for making HTTP API calls)
- SQL (for final query preparation)

## How to Run

1. Make sure you have Python 3 installed.
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
