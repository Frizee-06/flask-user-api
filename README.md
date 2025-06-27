#  Task 4 – REST API with Flask

This project is part of the Python Developer Internship program.

##  Objective
Create a simple *REST API using Flask* to manage user data with GET, POST, PUT, and DELETE endpoints.

##  Tools & Libraries Used
- Python
- Flask

##  Files in the Repository
- app.py → Flask API script
- README.md → Project documentation

##  How to Run the Flask API

###  Step 1: Install Flask

```bash
pip install flask

 Step 2: Run the App

python app.py

By default, Flask will run on http://127.0.0.1:5000

API Endpoints

Method	Endpoint	Description

GET	/users	Get all users
GET	/users/<id>	Get a specific user
POST	/users	Add a new user (JSON body)
PUT	/users/<id>	Update user details (JSON)
DELETE	/users/<id>	Delete a user

Example JSON for POST/PUT

{
  "name": "anis",
  "email": "anisfrizeela@gamil.com"
  "age":20 
}

 Testing the API

You can test this API using:

 Postman

 curl from terminal

 Any REST client/browser plugin
