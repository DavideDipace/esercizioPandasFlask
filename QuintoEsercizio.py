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
  labels = dfgroup['state']
  dati = dfgroup['customer_id']


  fig, ax = plt.subplots(figsize=(15,8))
  ax.bar(labels, dati, label='numero di clienti per ogni stato')
  ax.set_title('Titolo')
  ax.set_xlabel('stati')
  ax.set_ylabel('numero di clienti')
  dir = "static/images"
  file_name = "graf.png"
  save_path = os.path.join(dir, file_name)
  plt.savefig(save_path, dpi = 150)

  fig, b = plt.subplots(figsize=(15,8))
  b.barh(labels, dati, label='numero di clienti per ogni stato')
  b.set_title('Titolo')
  b.set_xlabel('stati')
  b.set_ylabel('numero di clienti')
  dir = "static/images"
  file_name = "graf2.png"
  save_path = os.path.join(dir, file_name)
  plt.savefig(save_path, dpi = 150)

  plt.figure(figsize=(15, 8))
  plt.pie(dati, labels=labels, autopct='%1.1f%%')
  dir = "static/images"
  file_name = "graf3.png"
  save_path = os.path.join(dir, file_name)
  plt.savefig(save_path, dpi = 150)
  return render_template('tabelle.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)