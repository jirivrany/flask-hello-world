import os
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)


@app.route("/")
def hello_world():
    user = os.getenv("DB_USER", "Not Found")
    remote_addr = request.remote_addr
    cookies = request.cookies
    cookies_str = ", ".join([f"{k}: {v}" for k, v in cookies.items()])
    return f"<p>Hello, World! And hello {user} from {remote_addr}</p><p>Cookies: {cookies_str}</p>"
