archivo = open('paises.txt', 'r')
#imprima la posicion de colombia

col=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  colombia=col+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(colombia)
archivo.close()