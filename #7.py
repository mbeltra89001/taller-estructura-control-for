archivo = open('paises.txt', 'r')
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U

lista=[]
ciudad=[]
for i in archivo:
  U=i.index(":")
  for r in range(U+2,len(i)):
    lista.append(i[r])
  U="".join(lista)
  ciudad.append(U)
  lista=[]
for i in ciudad:
  if(i[0]=="U"):
    print(i)
archivo = open('paises.txt', 'r')
lista2=[]
pais=[]
for i in archivo:
  paisU=i.index(":")
  for r in range(0,paisU):
    lista2.append(i[r])
  paisU="".join(lista2)
  pais.append(paisU)
  lista2=[]
for i in pais:
  if(i[0]=="U"):
    print(i)
archivo.close()