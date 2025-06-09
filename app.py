from flask import Flask
app = Flask(_name_)

@app.route("/")
def home():
    return "Hello from the cloud! This is my cloud deployment using Render."

import os

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000))  # use Render-assigned port
    app.run(host="0.0.0.0", port=port)