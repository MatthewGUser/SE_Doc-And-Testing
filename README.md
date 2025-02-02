# Auto Shop API

REST API with Swagger documentation and unit tests for managing auto shop mechanics.

## Project Structure

```
SE_Doc-And-Testing/
│── app/
│   │── blueprints/
│   │   │── __init__.py
│   │   │── mechanic.py
│   │── models/
│   │   │── __init__.py
│   │   │── mechanic.py
│   │── routes/
│   │   │── __init__.py
│   │   │── mechanic.py
│   │── static/
│   │   │── swagger.json
│   │── __init__.py
│   │── config.py
│   │── db.py
│── instance/
│   │── shop.db
│── tests/
│   │── __init__.py
│   │── test_mechanic.py
│── README.md
│── requirements.txt
│── run.py
```

## Setup Instructions

### Step 1: Create and Activate Virtual Environment

1. **Create virtual environment**:

```
python -m venv venv
```

2. **Activate virtual environment:**

```
venv\Scripts\activate
```

### **Step 2: Install Dependencies**

```
pip install -r requirements.txt
```

### **_Step 3: Initialize Database_**

```
flask init-db
```

### **_Step 4: Run the Server_**

```
python run.py
```

## **API Documentation**

Access Swagger UI at: `http://localhost:5000/swagger`

### API Endpoints

Mechanic Endpoints

- GET `/api/mechanics/`: Retrieve all mechanics
- GET `/api/mechanics/<id>`: Get mechanic by ID
- POST `/api/mechanics/`: Create new mechanic
- PUT `/api/mechanics/<id>`: Update mechanic
- DELETE `/api/mechanics/<id>`: Delete mechanic

### Testing

Run tests using:

```
python -m unittest discover tests
```

### **Database Schema**

**Mechanic**

- **id:** Integer (Primary Key)
- **name:** String (Required)
- **email:** String (Required, Unique)
- **specialty:** String
