import pandas as pd

url = 'https://raw.githubusercontent.com/rodtc22/1examen354/main/pregunta1/icpc.csv'
df = pd.read_csv(url, encoding="unicode_escape")

import matplotlib.pyplot as plt

x = df["Country"].value_counts().index.tolist() #de quien son los numeros
y = df["Country"].value_counts().tolist() #numeros

print(x)
print(y)

plt.bar(x,y)
plt.scatter(x,y)

plt.title("Participaciones") #a la final mundial icpc
plt.ylabel("No participaciones")
plt.xlabel("Pais")

plt.show()
plt.plot(x,y)