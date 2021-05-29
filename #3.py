archivo = open('paises.txt', 'r')
#Imprima todas las Capitales

lista=[]
for i in archivo:
  cap=i.index(":")
  for r in range(cap+2,len(i)):
    lista.append(i[r])
  capitalestotal="".join(lista)
  print(capitalestotal)
  lista=[]

archivo.close()