import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)


@app.route("/")
def hello_world():
    user = os.getenv("DB_USER", "Not Found")
    return f"<p>Hello, World! And hello {user}</p>"
