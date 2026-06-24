# CRM Storage System

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1-black?style=flat-square&logo=flask)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?style=flat-square)
![MySQL](htt (ps://img.shields.io/badge/MySQL-8.0-blue?style=flat-square&logo=mysql)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?style=flat-square&logo=bootstrap)

This is a web application (CRM/control panel) based on the Flask microframework. It enables automated inventory management, customer database maintenance, order management, and financial analysis.

## Main Features

- **Authentication and Security:** Secure registration and login system with password hashing (Flask-Login, Werkzeug).

- **Analytics Dashboard:** Main page displaying key metrics, revenue calculations, and recent activity metrics.

- **Order Management:** Full CRUD (Create, Read, Update, Delete) order management, convenient filtering by process, and contextual search.

- **Two Database Modes**: MySQL (for production environments via Docker) or lightweight SQLite (for fast local development).

- **Responsive Interface:** A modern responsive design based on Bootstrap 5 and Bootstrap icons, beautifully displayed on both desktop and mobile devices.

## 🛠 Technology Stack

* **Backend:** Python 3.11, Flask (Blueprint, Application Factory)
* **Database and ORM:** MySQL 8.0/SQLite, SQLAlchemy 2.0 (Flask-SQLAlchemy)
* **Frontend:** HTML5, Jinja2, Bootstrap 5, Bootstrap icons.

* **Infrastructure:** Docker, Docker Compose.

--

## Quick Start (Running with Docker)

This method is recommended for running this project. Docker Desktop must be installed and running.

### Step 1. Clone the Repository
``` bash
git clone https://github.com/your_username/flask_crm_app.git
flask_crm_app CD
```

### Step 2. Configure the Environment
Copy the `.env.example` configuration template to your working `.env` file.
``` bash
cp .env.example .env
```
*(You can change the default encryption key and MySQL database access credentials within the `.env` file)*

### Step 3. Run the Containers
Select the services (Flask Web Application and MySQL Database Server) and run them in the background.
``` bash
docker compose --build -d
```

### Step 4. Log in to the system
Once the database has been built and configured, perform the following steps in your browser:
**http://localhost:5000**

On the first launch, the necessary tables and test settings will be automatically installed. You will be redirected to the login page.

Use the default administrator credentials.
* **Login name:** `admin`
* **Password:** `admin`

---

## Development without Docker (Local Execution)

If you want to make changes to your local code without using Docker, follow these steps:

1. **Clone the repository** and use the project tools.

2. **Create and activate the virtual environment:**
``` bash python -m venv .venv
# For Windows: .venv\Scripts\activate
# For Linux/macOS: source .venv/bin/activate
```
3. **Install dependencies:**
``` bash pip install -r requirements.txt
```
4. **Database Setup:**
Ensure the `DATABASE_URL` line in your `.env` file is commented out. The application will automatically switch to the local SQLite database, and the database will be created in the crm.db file. 5. **Running Server Development:**
``` bash
flask run
# Or run directly from Python:
python run.py
```
---
## Project Architecture
This project is built modularly using Flask Blueprints templates.
`` ``` text
CRM system/
├── application/
│ ├── auth/ # Authentication module (login, registration, sessions)
│ ├── dashboard/ # Homepage module (metrics collection and display)
│ ├── routers/ # Additional routes and APIs
│ ├── static/ # Static files (CSS, JS, images)
│ ├── templates/ # HTML templates (base template and page components)
│ ├── __init__.py # Application initialization (Application Factory)
│ └── models.py # Description of SQLAlchemy models with established relationships
├── crm.db # Local SQLite database file (created when running locally)
├── docker-compose.yml # Configuration for running a multi-container application
├── Dockerfile # Docker image building script
├── require.txt # Python library dependencies
└── run.py # Entry point
```