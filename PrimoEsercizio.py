from flask import Flask, render_template, request

app = Flask(__name__)

import pandas as pd

df = pd.read_excel("https://github.com/wtitze/3E/blob/main/BikeStores.xls?raw=true", sheet_name = "customers")

@app.route('/')
def home():
  return render_template('PrimoEsercizio.html')

@app.route('/es1', methods = ['GET'])
def es1():
    nome = request.args.get('nome')
    cognome = request.args.get('cognome')
    df1 = df[(df["first_name"] == nome) & (df["last_name"] == cognome)].to_html()
    return render_template('Risultato1.html', tabella = df1)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)