print("LABORATORIO DE SUMA ACUMULATIVA")
x=input(print("ingresa la cantidad de numeros que vas a sumar: "))
x= int(x)

orden=[]
resultados=[]
y=1
n=0
a=0
while y<=x:
    a=a+1
    orden.append(a) #esta lista para X
    no=input(print("ingrese los numeros a sumar"))
    no=float(no) 
    n= no+n
    resultados.append(n) #esta lista para Y
    y=y+1
    
print(resultados)
print(orden)


import matplotlib.pyplot as ba

ba.barh(resultados,orden,color="green")

ba.xlabel("numero de entrada")
ba.ylabel("suma acumulativa correspondiente")
ba.title("Grafico de barras de suma acumulativa")
ba.show()