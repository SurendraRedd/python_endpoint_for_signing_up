# Flask Signup Application

This is a simple Flask application that provides an endpoint for user signup. The signup endpoint enforces strong passwords to ensure security.

## Features

- User signup with username and password
- Strong password validation
- In-memory user storage (for demonstration purposes)

## Password Requirements

A strong password must:
- Be at least 8 characters long
- Contain at least one uppercase letter
- Contain at least one lowercase letter
- Contain at least one digit
- Contain at least one special character

## Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/SurendraRedd/python_endpoint_for_signing_up.git
    cd python_endpoint_for_signing_up
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. **Start the Flask application**:
    ```bash
    python app.py
    ```

2. **Access the application**:
    - The application will be running at `http://127.0.0.1:5000`.

## Usage

You can test the signup endpoint using tools like Postman or cURL or bruno.

### Example cURL Request

```bash
curl -X POST http://127.0.0.1:5000/signup \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "password": "StrongPassword123!"}'
```
### bruno
<img width="781" alt="image" src="https://github.com/user-attachments/assets/0ae8d74f-8777-45c5-8865-6feca444f51a" />

