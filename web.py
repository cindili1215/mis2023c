from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    X = "作者:李欣諦<br>"
    X += "<a href=/mis>資管導論</a><br>"
    X += "<a href=/today>日期時間</a><br>"
    X += "<a href=/aboutme>李欣諦網頁</a><br>"
    return X

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"


@app.route("/aboutme")
def today():
    now = datetime.now()
    return render_template("aboutme.html", datetime = str(now)) 

if __name__ == "__main__":
    app.run()