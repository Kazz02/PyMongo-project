# Customer Management System

A full-stack customer management application built with Python, MongoDB, and FastAPI. 

## Features

* **REST API:** Built with FastAPI to create, read, and manage customers.
* **CLI Manager:** A terminal-based tool to manually add, view, update, and delete customers.
* **Data Seeding:** A script to populate the database with fake customer data for testing.
* **Data Export:** Functionality to export MongoDB data to CSV format.
* **Web Frontend:** A simple HTML + JS dashboard to view customers via the API.
* **MongoDB Integration:** Uses `pymongo` for efficient database interactions.

## Project Structure

* `api.py`: The main FastAPI application file defining endpoints.
* `customer_manager.py`: A CLI tool for interactive database management.
* `seed_data.py`: Script using `Faker` to generate test data.
* `export_data.py`: detailed script using `pandas` to export the database to `customers.csv`.
* `index.html`: A frontend interface that consumes the API to display a list of customers.
* `requirements.txt`: List of Python dependencies.

## Prerequisites

* **Python 3.7+**
* **MongoDB:** You must have MongoDB installed and running locally on the default port (`27017`).

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Kazz02/PyMongo-project.git
    cd your-repo-name
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ensure MongoDB is running:**
    Make sure your local MongoDB instance is active. The application connects to `mongodb://localhost:27017/` and uses a database named `mydatabase`.

## Usage

1. **Generating Test Data:**
If you want to start with some sample data, run the seed script:
```bash
python seed_data.py
``` 

2. **Running the API:**

To run the API, start the FastAPI server using Uvicorn:
```bash
uvicorn api:app --reload
```
The API will be available at http://127.0.0.1:8000. You can view the interactive API documentation at http://127.0.0.1:800/docs. 

3. **Using the web interface**

Once the API is running, you can open ```index.html``` in any web browser to view the customer list. The page fetches data from the API. The frontend will be updated.

4. **CLI management tool**

To manage customers directly from the termninal:
```bash
python customer_manager.py
```

5. **Exporting data to CSV file**
To export the current databse content to a CSV file:
```bash
python export_data.py
```
This will create a ```customers.csv``` file in the root directory

## API endpoints

- ```GET /```: root welcome message.
- ```GET /customers/```: retrieve all customers
- ```GET /customers/{name}```: retrieve a specific customer by name
- ```POST /customers/```: add a new customer

## Technologies used

- Python
- FastAPI
- MongoDB (PyMongo)
- Pandas (for data export)
- Faker (for data seeding)
- HTML/CSS/JavaScript

