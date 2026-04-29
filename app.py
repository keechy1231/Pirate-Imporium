from flask import Flask, render_template, request, redirect, url_for, session

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
            return redirect(url_for("shop"))

    return render_template("login.html")


@app.route("/shop")
def shop():
    if not session.get("username"):
        return redirect(url_for("login"))

    return render_template("shop.html", username=session["username"])


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/win")
def win():
    if not session.get("username"):
        return redirect(url_for("login"))

    return render_template("win.html")

if __name__ == "__main__":
    app.run(debug=True)