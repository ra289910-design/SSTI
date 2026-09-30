import os
from flask import Flask, render_template, render_template_string, request

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET", "ctf-development-secret")
app.config["CHALLENGE_FLAG"] = os.environ.get("CHALLENGE_FLAG", "flag{nfsu_jinja_ssti_template_escape_2026}")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/render", methods=["GET", "POST"])
def render():
    expression = request.values.get("name", "")
    # INTENTIONALLY VULNERABLE: user input is compiled as a Jinja template.
    rendered = render_template_string("Welcome, " + expression + "!", config=app.config)
    return render_template("result.html", rendered=rendered)

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("APP_PORT", "8090")))
