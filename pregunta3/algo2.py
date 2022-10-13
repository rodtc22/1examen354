import pandas as pd

#recupero mi csv desde github
url = 'https://raw.githubusercontent.com/rodtc22/1examen354/main/pregunta1/icpc.csv'
df = pd.read_csv(url, encoding="unicode_escape")

dataset = df.to_numpy()
fil = len(dataset)
col = len(dataset[0])

#preprocesamos datos str a enteros para poder usar otros algoritmos
from sklearn import preprocessing
labeler = preprocessing.LabelEncoder()

matriz = []
for j in range (col):
  c = dataset.T[j]
  if (type(c[0]) == str):
    label = labeler.fit_transform(c)    
    c = label
  matriz.append(c)

import numpy as np
matriz = np.array(matriz)
matriz = matriz.T

#----------------SEGUNDO ALGORITMO---------------
minmax = preprocessing.MinMaxScaler()
ans = minmax.fit_transform(matriz)

dfdatos2 = pd.DataFrame(ans, columns = df.columns)
dfdatos2
