from flask import Flask, render_template, request

app = Flask(__name__)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

df = pd.read_excel("https://github.com/wtitze/3E/blob/main/BikeStores.xls?raw=true", sheet_name = "customers")
dfgroup = df.groupby('state').count().reset_index()

@app.route('/')
def home():
  df6 = df[df["email"].isna()][["first_name","last_name","phone"]].to_html()

  return render_template('Risultato6.html', tabella = df6)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)