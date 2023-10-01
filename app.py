from flask import Flask, render_template, request
from language_tool_python import LanguageTool
from langdetect import detect

app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route('/', methods=['GET', 'POST'])
def correcteur():
    if request.method == 'POST':
        text = request.form['text']

        # Détection de la langue
        lang = detect(text)

        # Correction de grammaire en anglais si la langue est l'anglais, sinon correction en français
        if lang == 'en':
            tool = LanguageTool('en-US')
            corrected_text = tool.correct(text)
        else:
            tool = LanguageTool('fr')
            corrected_text = tool.correct(text)

        return render_template('result.html', text=text, corrected_text=corrected_text, detected_lang=lang)

    return render_template('correcteur.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Traitez le formulaire ici, en récupérant les données soumises par l'utilisateur
        nom = request.form['nom']
        email = request.form['email']
        sujet = request.form['sujet']
        message = request.form['message']
        
        # Ensuite, vous pouvez traiter ces données, par exemple, les enregistrer dans une base de données ou les envoyer par e-mail.

        # Une fois que le formulaire est soumis, vous pouvez rediriger l'utilisateur vers une page de confirmation ou une page de remerciement.
        return render_template('confirmation.html')
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)