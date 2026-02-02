from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

# --- CONFIGURATION CARTERPRONOSTIK ---
CONFIG = {
    "nom": "CARTERPRONOSTIK",
    "auteur": "STEPHENE MOUANDA DMS CARTER",
    "tel": "+242069647737",
    "tarif": "5000 FCFA / 3 MOIS"
}

# --- LISTE DES MATCHS (Avec logique Live et Floutage) ---
matchs_du_jour = [
    {"eq": "Niecieza vs Cracovia", "prono": "+1.5 Buts", "score": "2-1", "statut": "FINI", "val": "✅"},
    {"eq": "Udinese vs AS Roma", "prono": "Corners +8.5", "score": "5-3", "statut": "LIVE", "val": "⏳"},
    {"eq": "Sunderland vs Burnley", "prono": "+1.5 Buts", "score": "1-0", "statut": "LIVE", "val": "⏳"},
    # Matchs VIP (seront floutés)
    {"eq": "Mallorca vs Sevilla", "prono": "VIP", "score": "?-?", "statut": "VIP", "val": "🔒"},
    {"eq": "Gimnasia vs Aldosivi", "prono": "VIP", "score": "?-?", "statut": "VIP", "val": "🔒"},
    {"eq": "Casa Pia vs Porto", "prono": "VIP", "score": "?-?", "statut": "VIP", "val": "🔒"},
    {"eq": "Everton vs Union", "prono": "VIP", "score": "?-?", "statut": "VIP", "val": "🔒"}
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ c.nom }}</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #000; color: white; margin: 0; padding: 15px; }
        .header { background: linear-gradient(to bottom, #ffd700, #ff8c00); color: black; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 20px; }
        .card { background: #1a1a1a; padding: 15px; border-radius: 12px; margin-bottom: 12px; border-left: 5px solid #ffd700; position: relative; }
        .badge-live { background: red; color: white; padding: 2px 8px; border-radius: 5px; font-size: 0.7em; animation: blink 1s infinite; font-weight: bold; }
        @keyframes blink { 0% {opacity: 1;} 50% {opacity: 0.2;} 100% {opacity: 1;} }
        
        /* STYLE FLOUTAGE VIP */
        .blur-zone { filter: blur(5px); opacity: 0.5; pointer-events: none; }
        .vip-msg { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: #ffd700; font-weight: bold; z-index: 5; text-shadow: 2px 2px 5px black; }
        
        .btn-mtn { background: #ffcc00; color: black; padding: 15px; border-radius: 10px; text-decoration: none; font-weight: bold; display: block; text-align: center; margin-top: 20px; }
    </style>
</head>
<body>
    <div class="header">
        <h2 style="margin:0;">{{ c.nom }}</h2>
        <p style="margin:5px 0; font-size: 0.8em;">Par {{ c.auteur }}</p>
        <small>🇨🇬 {{ c.tel }}</small>
    </div>

    <h3>📊 Pronostics du {{ date }}</h3>

    {% for m in matchs %}
        {% if loop.index > 3 %}
        <div style="position: relative;">
            <div class="card blur-zone">
                <strong>{{ m.eq }}</strong><br>
                <small>Prono: {{ m.prono }}</small>
            </div>
            <div class="vip-msg">🔒 RÉSERVÉ VIP (5000 FCFA)</div>
        </div>
        {% else %}
        <div class="card">
            <span style="float: right;">{{ m.val }}</span>
            <strong>{{ m.eq }}</strong> 
            {% if m.statut == 'LIVE' %}<span class="badge-live">DIRECT</span>{% endif %}<br>
            <span style="color:#ffd700;">🎯 Prono: {{ m.prono }}</span><br>
            <small>Score: {{ m.score }} ({{ m.statut }})</small>
        </div>
        {% endif %}
    {% endfor %}

    <div style="background: #004a99; padding: 20px; border-radius: 15px; margin-top: 25px; border: 2px solid #ffcc00;">
        <h3 style="text-align:center; margin:0;">🚀 DÉBLOQUER LES 12 MATCHS</h3>
        <p style="text-align:center; font-size: 0.9em;">Essai gratuit 1 semaine puis {{ c.tarif }}</p>
        <a href="tel:{{ c.tel }}" class="btn-mtn">PAYER VIA MTN CONGO 🇨🇬</a>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, c=CONFIG, matchs=matchs_du_jour, date=datetime.now().strftime("%d/%m/%Y"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)