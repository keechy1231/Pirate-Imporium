from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"

USERS = {
    "user": "user123",
    "admin": "admin123"
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in USERS and USERS[username] == password:
            session["username"] = username
            session["balance"] = 1000
            return redirect(url_for("shop"))
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")


@app.route("/shop")
def shop():
    username = session.get("username")
    if not username:
        return redirect(url_for("login"))

    balance = session.get("balance", 0)

    return render_template("shop.html", username=username, balance=balance)


@app.route("/checkout", methods=["POST"])
def checkout():
    username = session.get("username")
    if not username:
        return redirect(url_for("login"))

    total = int(request.form.get("total", 0))
    items = request.form.get("items", "")

    balance = session.get("balance", 0)

    if total <= balance:
        balance -= total
        session["balance"] = balance

        flag = ""
        if "parrot" in items:
            flag = "FLAG{pirate_parrot_loyalty}"

        return render_template(
            "checkout.html",
            total=total,
            balance=balance,
            flag=flag
        )

    return render_template(
        "checkout.html",
        total=total,
        balance=balance,
        flag="Not enough gold!"
    )


@app.route("/my-account")
def account():
    username = session.get("username")
    if not username:
        return redirect(url_for("login"))

    return render_template("account.html", username=username)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)