# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template, url_for, request, session, redirect

import json
import socket


# flask settings
app = Flask(__name__, static_url_path="")


# web pages
@app.route("/")
def homepage():
    return "hello test drone"


if __name__ == "__main__":
    app.run()
