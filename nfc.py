from flask import Flask, request, redirect, abort, render_template_string
import secrets
import time
import os  # <- wichtig für Render-Port

app = Flask(__name__)
TOKEN_LIFETIME = 60  # Sekunden
valid_tokens = {}

@app.route('/token/anfrage')
def token_anfrage():
    # Token erstellen
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

    # Token nach erstem Zugriff löschen
    del valid_tokens[token]

    # Visitenkarte anzeigen
    return render_template_string("""
        <h1>👋 Hallo, das ist meine digitale Visitenkarte</h1>
        <p><strong>Name:</strong> Max Mustermann</p>
        <p><strong>Email:</strong> max@example.com</p>
        <p><strong>LinkedIn:</strong> <a href="https://linkedin.com/in/max">Mein Profil</a></p>
    """)

@app.route('/')
def index():
    return '<p>⛔ Kein Zugriff. Bitte scanne meinen NFC-Chip.</p>'

if __name__ == "__main__":
    # Für Render: App auf 0.0.0.0 und dynamischem Port starten
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
