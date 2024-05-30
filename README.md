# Activate the virtual environment (PowerShell)
.\venv\Scripts\Activate.ps1
# Install FastAPI and uvicorn
pip install fastapi uvicorn

# Install motor for MongoDB
pip install motor
# FastAPI MongoDB Project

This project is a simple REST API built using FastAPI and MongoDB. It provides CRUD operations for managing items.

## Installation

1. Clone this repository:

```bash
git clone https://github.com/your_username/fastapi-mongodb-project.git
cd fastapi-mongodb-project
python3 -m venv venv
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
## Endpoints
POST /items/: Create a new item.
GET /items/{item_id}/: Retrieve an item by ID.
PUT /items/{item_id}/: Update an item by ID.
DELETE /items/{item_id}/: Delete an item by ID.
