from flask import Flask, render_template, request, redirect, url_for
from waitress import serve  

app = Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for("signup"))

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        card_number = request.form["card_number"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            return render_template("signup.html", error="Passwords do not match", name=first_name, lastname=last_name, email=email, cardnumber=card_number)

        return render_template("index.html")

    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        return f"Welcome, {email}!"

    return render_template("login.html")

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
