# Flask API and Test Script

This repository contains a simple Flask API and a corresponding test script for making HTTP requests to the API endpoints. The Flask API handles both POST and GET requests and includes a home screen rendered using HTML templates.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Contributing](#contributing)
- [License](#license)


## Flask API

## Introduction

The Flask API is a simple Python application that utilizes the Flask framework to create a basic web API. It includes two endpoints, one for handling POST requests and another for handling GET requests. The application also features a home screen.

## Requirements
- Request package
- Flask package
- Colorama (optional)

## Installations

1. **Clone Repository**

   ```bash
   https://github.com/FinesserULTRA/Custom-Flask-API.git
   ```
2. **Get Required Packages**

   ```bash
   pip install requests, flask, colorama
   ```

3. **Change directory**

   ```bash
   cd Custom-Flask-API
   ```

## Usage

1. **Run the program:**

    ```bash
    python main.py
    ```
    ```bash
    python Requests.py
    ```

2. **Access the different endpoints**

    - Visit http://127.0.0.1:5000 to view the home screen.
    - http://127.0.0.1:5000/test for GET test page.
    - http://127.0.0.1:5000/POST is the POST endpoint, cant be accessed from web. 

3. **Interact With API**

   - Use `main.py` to run server/api.
   - Use `Requests.py` to send POST and GET requests to API


## Endpoints

### `POST Endpoint`

- URL: `/POST`
- Method: POST
- Request Body:
    ```bash
    {
    "name": "YourName"
    }
    ```
- Response:
    ```bash
    {
    "name": "Hello, YourName! How are you?"
    }
    ```
- Error Response:
    ```bash
    {
    "error": "You must provide a name, you fool"
    }
    ```

### `GET Endpoint`

- URL: `/test`
- Method: GET
- Response:
    ```bash
    {
    "test": "this is a test bro"
    }
    ```    
### `Home Screen`

- URL: `/`
- Displays a basic home screen.
  
## Contributing

Contributions are welcome! If you have any ideas, improvements, or bug fixes, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
