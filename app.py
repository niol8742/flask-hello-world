from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World from Nick OLeary in 3308"
