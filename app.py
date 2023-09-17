from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


@app.route("/planejar")
def planejar():
    return render_template("planejar.html")


@app.route("/resultado")
def resultado():
    return render_template("resultado.html")


@app.route("/naoEncontrado")
def naoEncontrado():
    return render_template("naoEncontrado.html")


if __name__ == "__main__":
    app.run(debug=True)

# py app.py inicia a aplicação
# ctrl+c desliga a aplicação
