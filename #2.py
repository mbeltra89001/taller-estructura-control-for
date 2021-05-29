archivo = open('paises.txt', 'r')
#Imprima todos los paises

lista=[]
for i in archivo:
  paises=i.index(":")
  for r in range(0,paises):
    lista.append(i[r])
  listtotal="".join(lista)
  print(listtotal)
  lista=[]
archivo.close()