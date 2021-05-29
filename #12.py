#Busque e imprima la Capiltal de Colombia
archivo = open('paises.txt', 'r')
lisT=[]
for i in archivo:
  list.append(i)
  capcolombia=" ".join(list)
  if(capcolombia=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(capcolombia)
archivo.close()