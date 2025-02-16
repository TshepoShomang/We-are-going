from flask import Flask, render_template, request, redirect, url_for
from waitress import serve  

app = Flask(__name__)

first_name = None
last_name = None
email = None
card_number = None


@app.route("/")
def home():
    return redirect(url_for("signup"))

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        global first_name
        first_name = request.form["first_name"]
        global last_name
        last_name = request.form["last_name"]
        global email
        email = request.form["email"]
        global card_number
        card_number = request.form["card_number"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            return render_template("signup.html", error="Passwords do not match", name=first_name, lastname=last_name, email=email, cardnumber=card_number)

        return redirect(url_for("index"))

    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        return redirect(url_for("index"))

    return render_template("login.html")


@app.route("/index", methods=["GET", "POST"])
def index():
    if first_name != "" or first_name != None:
        return render_template("index.html", name=first_name, lastname=last_name, cardnumber=card_number)
    return redirect(url_for("/"))

@app.route("/tapping")
def tapping():
    return render_template("tap.html")

if __name__ == "__main__":
    #serve(app, host="0.0.0.0", port=5000)
    app.run(debug=True)
