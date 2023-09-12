from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/planejar")
def planejar():
    return render_template("planejar.html")


if __name__ == "__main__":
    app.run(debug=True)

# py app.py inicia a aplicação
# ctrl+c desliga a aplicação
# freCodeCamp "criando uma aplicação web simples"
