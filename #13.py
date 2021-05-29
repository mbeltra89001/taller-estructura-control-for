archivo = open('paises.txt', 'r')
#imprima la posicion del pais de Uganda
Uganda=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  Ug=Uganda+1 
  if(a=="Uganda: Kampala\n"):
    break
  lista=[]   
print(Ug)
archivo.close()