import os
from flask import Flask, request, render_template
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)


@app.route("/")
def hello_world():
    user = os.getenv("DB_USER", "Not Found")
    remote_addr = request.remote_addr
    cookies = request.cookies
    headers = request.headers
    return render_template("debug.html", user=user, remote_addr=remote_addr, cookies=cookies, headers=headers)
