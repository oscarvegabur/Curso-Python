#En este codigo lo que se busca es que el usuario nos proporcione dos coordenadas.

#se le pide al usuario que nos de dos alores numericos entero para graficarlos.

x = int(input("ingresa la coordenada x por favor:"))
y = int(input("ingresa la coordenada y por favor:"))

#una vez ingresados los valores de X y Y tenemos que categorizar los ejes y cuadrantes.

if x == 0 and y == 0:
    print("Los valores no pueden ser 0")
if x == 0:
    print("Lo siento el valor de X no puede ser 0 intentalo otravez")
if y == 0:
    print("Lo siento el valor de Y no puede ser 0 intentalo otravez")
if x > 0 and y > 0:
    print("Estas en el primer cuadrante")
if x < 0 and y > 0:
    print("Estas en el segundo cuadrante")
if x < 0 and y < 0:
    print("Estas en el tercer cuadrante")
if x > 0 and y < 0:
    print("Estas en el cuarto cuadrante")