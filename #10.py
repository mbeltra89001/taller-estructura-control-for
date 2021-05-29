archivo = open('paises.txt', 'r')
#Busque e imprima el pais de Venezuela y su capital

lista=[]
for i in archivo:
  lista.append(i)
  ven=" ".join(lista)
  if(ven=="Venezuela: Caracas\n"):
    break
  lista=[]   
print(ven)
archivo.close()