from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    X = "作者:李欣諦<br>"
    X += "<a href=/mis>資管導論</a><br>"
    X += "<a href=/today>日期時間</a><br>"
    X += "<a href=/aboutme>欣諦網頁</a><br>"
    X += "<a href=/welcome?guest=cindy>歡迎我</a><br>"
    X += "<a href=/account></a>使用表單上傳值</a><br>"

    return X

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html", datetime = str(now))

@app.route("/aboutme")
def about():
    return render_template("aboutme.html") 

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("guest")
    return render_template("welcome.html")

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")


if __name__ == "__main__":
    app.run()