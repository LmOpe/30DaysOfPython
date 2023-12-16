# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://LmOpe:Muhammed35@30daysofpython.tjsoqih.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

db = client['thirty_days_of_python'] # accessing the database

student = db.students.find_one()
print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)