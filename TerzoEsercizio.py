from flask import Flask, render_template, request

app = Flask(__name__)

import pandas as pd

df = pd.read_excel("https://github.com/wtitze/3E/blob/main/BikeStores.xls?raw=true", sheet_name = "customers")

@app.route('/')
def home():
  return render_template('TerzoEsercizio.html')

@app.route('/es3', methods = ['GET'])
def Es3():
  df3 = df.groupby('state').count().reset_index().to_html()
  return render_template('Risultato3.html', tabella = df3)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)