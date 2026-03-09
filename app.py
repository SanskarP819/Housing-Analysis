from flask import Flask, render_template
import os

app = Flask(__name__)


def _get_tableau_url() -> str:
    """Use env var so the embed can be wired to Tableau Public/Server later."""
    return os.getenv("TABLEAU_EMBED_URL", "")


@app.route("/")
def index():
    tableau_url = _get_tableau_url()
    return render_template("index.html", tableau_url=tableau_url)


if __name__ == "__main__":
    app.run(debug=True)
