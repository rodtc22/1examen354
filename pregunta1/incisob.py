import pandas as pd

#recupero mi csv desde github
url = 'https://raw.githubusercontent.com/rodtc22/1examen354/main/pregunta1/icpc.csv'
df = pd.read_csv(url, encoding="unicode_escape")

#-------------CON PANDAS----------------
print("Calculo del cuantil 1:")
print(df.quantile(0.25))
print()

print("Calculo del percentil 90:")
print(df.quantile(0.9))
print()

print("Calculo del percentil 95:")
print(df.quantile(0.95))
print()

#-------------CON NUMPY----------------
import pandas as pd
import numpy as np

#recupero mi csv desde github
url = 'https://raw.githubusercontent.com/rodtc22/1examen354/main/pregunta1/icpc.csv'
df = pd.read_csv(url, encoding="unicode_escape")

dataset = df.to_numpy() # voy a usar la transpuesta para obtener la columna j-esima

nrofil = len(dataset)
nrocol = len(dataset[0])


print("Calculo del cuantil 1:")
for j in range(nrocol) :
  if (type(dataset[0][j]) == str):
    continue
  col = dataset.T[j]
  col.sort()
  print(np.quantile(col, 0.25))
print()
  
print("Calculo del percentil 90:")
for j in range(nrocol) :
  if (type(dataset[0][j]) == str):
    continue
  col = dataset.T[j]
  col.sort()
  print(np.quantile(col, 0.90))
print()

  
print("Calculo del percentil 95:")
for j in range(nrocol) :
  if (type(dataset[0][j]) == str):
    continue
  col = dataset.T[j]
  col.sort()
  print(np.quantile(col, 0.95))
print()