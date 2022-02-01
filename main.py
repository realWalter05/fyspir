from flask import Flask, render_template, request
from homework_writer import HomeworkWriter

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    print("here")
    ok_ltrs = request.args.getlist("ok_ltrs")
    need_ltr = request.args.get("need_ltr")
    eng = request.args.get("eng")
    capitals = request.args.get("capitals")
    seperator = request.args.get("seperator")
    min_length_word = request.args.get("min_length_word")
    length = request.args.get("length")

    if ok_ltrs and need_ltr:
        ok_ltrs = str(''.join(str(l) for l in ok_ltrs))

        h = HomeworkWriter(ok_ltrs, str(need_ltr), bool(eng), bool(capitals), str(seperator), min_length_word, length) 
        return render_template("index.html", homework=h.text)

    print("nope")

    return render_template("index.html", homework="")
