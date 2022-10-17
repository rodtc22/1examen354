from kanren import facts, Relation, var, run
import numpy as np
#son declaraciones de variables especiales, que sierven para trabajar con las relaciones
a = var() 
b = var()

#Relacion padres
padres = Relation()
facts (padres,
("Alberto", "Alex"), ("Alberto", "Elsa"), ("Alberto", "Fernando"), ("Alberto", "Monica"), 
("Benedicto", "Gregorio"), ("Benedicto", "Jorge"), 
("Carmen", "Alex"), ("Carmen", "Elsa"), ("Carmen", "Fernando"), ("Carmen", "Monica"), 
("Gregorio", "Cristina"), ("Gregorio", "Humberto"), ("Gregorio", "Lucio"), ("Gregorio", "Magali"), 
("Irene", "Cristian"), ("Irene", "Lourdes"), ("Irene", "Rodrigo"), 
("Jorge", "Cristian"), ("Jorge", "Lourdes"), ("Jorge", "Rodrigo"), 
("Juana", "Alberto"), ("Juana", "Irene"), ("Juana", "Leonor"), 
("Leonor", "Jimmy"), ("Leonor", "Lizeth"), ("Leonor", "Pamela"), ("Leonor", "Victor"), 
("Maximo", "Alberto"), ("Maximo", "Irene"), ("Maximo", "Leonor"), 
("Sabina", "Cristina"), ("Sabina", "Humberto"), ("Sabina", "Lucio"), ("Sabina", "Magali"), 
("Vicente", "Jimmy"), ("Vicente", "Lizeth"), ("Vicente", "Pamela"), ("Vicente", "Victor"), 
)

#Relacion abuelos
abuelos = Relation()
facts (abuelos,
("Benedicto", "Cristian"), ("Benedicto", "Cristina"), ("Benedicto", "Humberto"), ("Benedicto", "Lourdes"), ("Benedicto", "Lucio"), ("Benedicto", "Magali"), ("Benedicto", "Rodrigo"), 
("Juana", "Alex"), ("Juana", "Cristian"), ("Juana", "Elsa"), ("Juana", "Fernando"), ("Juana", "Jimmy"), ("Juana", "Lizeth"), ("Juana", "Lourdes"), ("Juana", "Monica"), ("Juana", "Pamela"), ("Juana", "Rodrigo"), ("Juana", "Victor"), 
("Maximo", "Alex"), ("Maximo", "Cristian"), ("Maximo", "Elsa"), ("Maximo", "Fernando"), ("Maximo", "Jimmy"), ("Maximo", "Lizeth"), ("Maximo", "Lourdes"), ("Maximo", "Monica"), ("Maximo", "Pamela"), ("Maximo", "Rodrigo"), ("Maximo", "Victor"), 
)


def fpadres (yo):
  tup = run(2,a,padres(a,yo))
  ans = [x for x in tup]
  ans = np.unique(ans)
  return ans

def fhijos(yo):
  tup = run(99, a, padres(yo, a))
  ans = [x for x in tup]
  ans = np.unique(ans)
  return ans

def fabuelos (yo):
  p = fpadres(yo)
  ans = []
  for x in p :
    tup = run(2,a,padres(a, x))
    for y in tup:
      ans.append(y) #solo para ponerlo en una lista
  ans = np.unique(ans)
  return ans

def ftios (yo):
  ab = fabuelos(yo)
  pa = fpadres(yo)

  ans = []
  for x in ab:
    tup = run(99, a, padres(x, a))
    for y in tup:
      if (not(y == pa[0]) and not (y == pa[1])):
        ans.append(y)

  ans = np.unique(ans)
  return ans

def fprimos (yo):
  ti = ftios(yo)
  ans = []
  for x in ti:
    tup = run(99, a, padres(x, a))
    for y in tup:
      ans.append(y)
  ans = np.unique(ans)
  return ans

def ftios2 (yo):
  ti = fprimos(yo)
  ans = []
  for x in ti:
    tup = run(2, a, padres(a, x))
    for y in tup:
      ans.append(y)
  ans = np.unique(ans)
  return ans


def datosPersona(yo):
  print("PADRES: ", fpadres(yo))
  print("ABUELOS: ", fabuelos(yo))
  print("TIOS: ", ftios(yo))
  print("PRIMOS: ", fprimos(yo))
  print()

print("HIJOS DE JORGE ", fhijos("Jorge"))

persona1 = "Rodrigo"
print("TIOS2: ", ftios2(persona1))
datosPersona(persona1)


persona2 = "Alex"
datosPersona(persona2)
