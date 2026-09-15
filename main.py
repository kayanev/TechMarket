# Atalho no VS Code: Ctrl+Shift+B roda o Flask com debug (uv run flask --app main run --debug)

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """Renderiza a pagina principal."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
