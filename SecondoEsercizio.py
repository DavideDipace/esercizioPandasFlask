from flask import Flask, render_template, request

app = Flask(__name__)

import pandas as pd

df = pd.read_excel("https://github.com/wtitze/3E/blob/main/BikeStores.xls?raw=true", sheet_name = "customers")

@app.route('/')
def home():
  l = df["city"].to_list()
  return render_template('citta.html', lista = list(set(l)))

@app.route('/<citta>', methods = ['GET'])
def Es2(citta):
  df2 = df[df["city"] == citta].to_html()
  return render_template('Risultato1.html', tabella = df2)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)