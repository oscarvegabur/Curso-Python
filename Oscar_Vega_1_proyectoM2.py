#COMIENZO DEL CODIGO PARA VERIFICAR LA LONGITUD DE UNA PALABRA QUE TIENE QUE TENER ENTRE 4 Y 8 CARACTERES.
#se le pide al usuario introducir su palabra

palabra = input ("Introduce una plabra por favor: ")

#En este paso se guarda en la variable "l" la longitud de la palabra
l=len(palabra)
#En los siguientes codigos se categoriza que repuesta darle al usuario dependiendo de la longitud de su palabra.
if l <= 3:
  print(f"Hacen falta letras. Tienes {l} letras en tu palabra")
if l >= 4 and l <= 8:
  print(f"La palabra esta en el rango correcto y tiene {l} letras.")
if l > 8:
  print(f"Sobran letras. Tienes {l} letras en tu palabra ")
