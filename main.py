from flask import Flask, render_template, request
from homework_writer import HomeworkWriter

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    return render_template("index.html", homework="")
