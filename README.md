# HNGx Task 2

## 🏁 Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Setting up a development environment
#### Step 1: Clone the repository

```bash
https://github.com/RansfordGenesis/hngx-task-2.git
```

#### step 2: Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

```

#### Step 3: Install dependencies

```
pip install -r requirements.txt
```

#### Step 4: Start the uvicorn server

```bash
uvicorn main:app --reload
```


## ✏️ Endpoints

Endpoints

### *Create a Person*

- Request Method: POST

- Endpoint: /api

- Response Code: 201 CREATED

- Request Body:

```json
{
    "name": "Ransford Genesis"
}
``````
- Sample Response:

```json
{
    "id": 1,
    "name": "Ransford Genesis"
}
```

### *Retrieve a Person*

- Request Method: GET

- Endpoint: /api/{id}

- Response Code: 200 OK

- Sample Response:

```json
{
    "id": 1,
    "name": "John Doe"
}
```

### *Update Details of a Person*

- Request Method: PUT

- Endpoint: /api/{id}

- Response Code: 200 OK

- Request Body:

```json
{
    "name": "Kwaku Gene"
}
```
- Sample Response:

```json
{
    "id": 1,
    "name": "Kwaku Gene"
}
```

### *Delete a Person*

- Request Method: DELETE

- Endpoint: /api/{id}

- Response Code: 200 OK

- Sample Response:

```json
{
  "message": "Person deleted successfully"
}
```

## ⚙️ Testing
> You can test the API using tools like Postman or by sending HTTP requests to the specified endpoints.

## 📋 Structure

```lua
- Root
  |
  +-- schemas
  |     |
  |     +-- schemas.py
  |     |
  |     +-- __init__.py
  |
  +-- utils
  |     |
  |     +-- crud.py
  |     |
  |     +-- __init__.py
  |
  +-- database
  |     |
  |     +-- database.py
  |     |
  |     +-- models.py
  |     |
  |     +-- __init__.py
  |
  +-- readme.md
  |
  +-- sql_app.db
  |
  +-- main.py
  |
  +-- requirements.txt
  |
  +-- license
  |
  +-- .gitignore
```