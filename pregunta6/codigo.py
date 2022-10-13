import pandas as pd

#recupero mi csv desde github
url = 'https://raw.githubusercontent.com/rodtc22/1examen354/main/pregunta1/icpc.csv'
df = pd.read_csv(url, encoding="unicode_escape")

dataset = df.to_numpy()
fil = len(dataset)
col = len(dataset[0])

#----------------PRIMER ALGORITMO---------------
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

dfdatos = pd.DataFrame(matriz, columns=df.columns)

#seleccionamos variables
explicativas = dfdatos.drop(columns = "num_of_top_100_last_20_year")
objetivo = df.num_of_top_100_last_20_year

# print(explicativas)
# print(objetivo)


#entrenar modelo
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(max_depth=4)
model.fit(X=explicativas, y=objetivo)
DecisionTreeClassifier()

#visualizar modelo
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
plt.figure(figsize=(20, 10))
plot_tree(decision_tree=model, feature_names=explicativas.columns, filled = True, fontsize=10); #este punto y coma para que no muestre el texto que suele salir



