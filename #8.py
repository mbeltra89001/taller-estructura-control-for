archivo = open('paises.txt', 'r')
#Cuente e imprima cuantos paises que hay en el archivo
Paises=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  P=Paises+1 
  if(a=="Paises\n"):
    break
  lista=[]   
print(P)
archivo.close()