archivo = open('paises.txt', 'r')
#imprima todas las capitales que inicien con la leta B

lista=[]
ciudad=[]
for i in archivo:
  B=i.index(":")
  for r in range(B+2,len(i)):
    lista.append(i[r])
  B="".join(lista)
  ciudad.append(B)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)  

archivo.close()