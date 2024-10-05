#se piden los datos a la persona

n = input ("Su nombre porfavor:")
e = int (input ("Introduzca su edad:"))
a = float (input("Introduca su altura en metros:"))
m = float (input("Introduzca su peso en KG:"))
est = a     
IMC = m / est**2 #Se hace el calculo del IMC
if(e<18):
        print("Eres Menor de edad")
else:
        print("Eres Mayor de edad")
if IMC >= 0  and IMC < 18.5: #se clasifican los indices de peso
        Indice =  "Bajo peso"
elif IMC> 18.5 and IMC < 24.9:
        Indice = "Peso Saludable"
elif IMC> 25.0 and IMC < 29.9:
        Indice = "Sobrepeso"
elif IMC>= 30.00:
        Indice = "Obesidad"
print(f"Tu nombre es: {n}, Tienes {e} años de edad." ) # se imprime nombre y edad
print(f"Su IMC es: {IMC:.2f}") # se imprime el imc de la persona
print(f"Su Clasificacion es: {Indice}") # se imprime la clasificacion de la persona