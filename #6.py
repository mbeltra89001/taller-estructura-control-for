archivo = open('paises.txt', 'r')
#Cuente e imprima cuantas ciudades inician con la latra M
lista=[]
lista3=[]
ciudad=[]
for i in archivo:
  M=i.index(":")
  for r in range(M+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="M"):
    lista3.append(i)
    total=len(lista3)
    print(total)
archivo.close()