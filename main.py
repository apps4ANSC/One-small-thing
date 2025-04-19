from flask import Flask, render_template, request, redirect
import random
from datetime import datetime

app = Flask(__name__)

translations = {
    'en': {'title': 'One Small Thing', 'button': 'I did it', 'counter': 'people did one small thing today'},
    'fr': {'title': 'Une Petite Chose', 'button': "Je l'ai fait", 'counter': "personnes ont fait une petite chose aujourd'hui"}
}

actions = [
    {'en': {'text': 'Smile at yourself in the mirror.', 'why': 'Self-directed kindness ripples outward.'},
     'fr': {'text': 'Souriez-vous dans le miroir.', 'why': 'La gentillesse envers soi-même rayonne vers l’extérieur.'}},
    {'en': {'text': 'Drink a full glass of water — slowly.', 'why': 'It’s not just hydration. It’s a way to come back to your body.'},
     'fr': {'text': 'Buvez un verre d’eau complet — lentement.', 'why': 'Ce n’est pas que de l’hydratation. C’est une façon de revenir à son corps.'}}
]

daily_count = 0
last_reset_date = datetime.now().date()

@app.route('/')
def home():
    global daily_count, last_reset_date
    current_date = datetime.now().date()
    if current_date > last_reset_date:
        daily_count = 0
        last_reset_date = current_date

    lang = request.args.get('lang', 'en')
    if lang not in translations:
        lang = 'en'

    return render_template('index.html',
                           action=random.choice(actions),
                           count=daily_count,
                           lang=lang,
                           translations=translations)

@app.route('/done')
def done():
    global daily_count
    daily_count += 1
    lang = request.args.get('lang', 'en')
    return redirect(f"/?lang={lang}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)