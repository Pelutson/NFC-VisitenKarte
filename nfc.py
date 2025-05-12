from flask import Flask, request, redirect, abort, render_template
import secrets
import time
import os

app = Flask(__name__)
TOKEN_LIFETIME = 60  # Sekunden
valid_tokens = {}

@app.route('/token/anfrage')
def token_anfrage():
    token = secrets.token_urlsafe(12)
    valid_tokens[token] = time.time() + TOKEN_LIFETIME
    print(f"Token erstellt: {token}")
    return redirect(f"/visitenkarte?token={token}")

@app.route('/visitenkarte')
def visitenkarte():
    token = request.args.get("token")
    if not token or token not in valid_tokens:
        return abort(403)

    if time.time() > valid_tokens[token]:
        del valid_tokens[token]
        return abort(403)

    del valid_tokens[token]
    return render_template("visitenkarte.html")  # Lädt HTML-Datei aus /templates

@app.route('/')
def index():
    return '<p>⛔ Kein Zugriff. Bitte scanne meinen NFC-Chip.</p>'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
