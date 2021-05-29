archivo = open('paises.txt', 'r')
#imprima la posicion del pais de Mexico
mex=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  orale=mex+1 
  if(a=="México: Ciudad de México \n"):
    break
  lista=[]   
print(orale)
archivo.close()