from flask import Flask, render_template, request, redirect, url_for, session
import json

app = Flask(__name__)
app.secret_key = "supersecretkey"

USERS = {"user": "user123"}


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in USERS and USERS[username] == password:
            session["username"] = username
            session["balance"] = 1000
            return redirect(url_for("shop"))

    return render_template("login.html")


@app.route("/shop")
def shop():
    if not session.get("username"):
        return redirect(url_for("login"))

    return render_template(
        "shop.html",
        username=session["username"],
        balance=session["balance"]
    )


@app.route("/checkout", methods=["POST"])
def checkout():
    if not session.get("username"):
        return redirect(url_for("login"))

    items = request.form.get("items", "").split(",")

    prices = {
        "sword": 100,
        "chest": 250,
        "parrot": 5000
    }

    total = 0

    for item in items:
        if item in prices:
            total += prices[item]
        else:
            return "Invalid item", 400

    balance = session["balance"]

    if total <= balance:
        session["balance"] -= total

        flag = ""

        # ✅ NEW LAB CONDITION
        if "parrot" in items and total < 1000:
            flag = "FLAG{pirate_parrot_loyalty}"

        return render_template(
            "checkout.html",
            total=total,
            balance=session["balance"],
            flag=flag
        )

    return render_template(
        "checkout.html",
        total=total,
        balance=balance,
        flag="Not enough gold!"
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/my-account")
def account():
    if not session.get("username"):
        return redirect(url_for("login"))

    return render_template("account.html", username=session["username"])


if __name__ == "__main__":
    app.run(debug=True)