import os
from flask import Flask, request, render_template
from dotenv import load_dotenv
from werkzeug.middleware.proxy_fix import ProxyFix


load_dotenv()  # take environment variables from .env.

app = Flask(__name__)
# we are behind a proxy, so we need to tell Flask to trust the X-Forwarded- headers
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)


@app.route("/")
def hello_world():
    user = os.getenv("DB_USER", "Not Found")
    remote_addr = request.remote_addr
    cookies = request.cookies
    headers = request.headers
    return render_template("debug.html", user=user, remote_addr=remote_addr, cookies=cookies, headers=headers)
