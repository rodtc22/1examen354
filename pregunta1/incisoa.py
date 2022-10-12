import pandas as pd

#recupero mi csv desde github
import pandas as pd

#recupero mi csv desde github
url = 'https://raw.githubusercontent.com/rodtc22/1examen354/main/pregunta1/icpc.csv'
df = pd.read_csv(url, encoding="unicode_escape")

dataset = df.to_numpy()

nrofilas = len(dataset)
nrocol = len(dataset[0])


#calculamos el 1er cuartil
for j in range(nrocol):
  if (type(dataset[0][j]) == str):
     continue
  col = []
  for i in range(nrofilas):
    col.append(dataset[i][j])

  col.sort()
  
  pos = (1 * (nrofilas + 1)) / 4
  if (pos % 4 == 0) :
    print(col[pos-1])
  else:
    entera = int(pos)
    d = pos - entera

    xi = col[entera-1]
    xi_1 = col[entera];

    q = xi + d * (xi_1 - xi)
    print(q)
print()

#calculamos en percentil 90
for j in range(nrocol):
  if (type(dataset[0][j]) == str):
     continue
  col = []
  for i in range(nrofilas):
    col.append(dataset[i][j])
  
  col.sort()

  pos = (90 * (nrofilas + 1)) / 100
  if (pos % 100 == 0) :
    print(col[pos-1])
  else:
    entera = int(pos)
    d = pos - entera

    xi = col[entera-1]
    xi_1 = col[entera];

    q = xi + d * (xi_1 - xi)
    print(q)
print()

#calculamos el percentil 95
for j in range(nrocol):
  if (type(dataset[0][j]) == str):
     continue
  col = []
  for i in range(nrofilas):
    col.append(dataset[i][j])
  
  col.sort()

  
  pos = (95 * (nrofilas + 1)) / 100
  if (pos % 100 == 0) :
    print(col[pos-1])
  else:
    entera = int(pos)
    d = pos - entera

    xi = col[entera-1]
    xi_1 = col[entera];

    q = xi + d * (xi_1 - xi)
    print(q)

print()