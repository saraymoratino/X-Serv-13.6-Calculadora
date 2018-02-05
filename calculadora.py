#Saray Moratino Sousa
#!/usr/bin/python3

import sys

operacion = sys.argv[1]
try:
	num1 = int(sys.argv[2])
	num2 = int(sys.argv[3])
except ValueError:
	print("Algun operando incorrecto.")

if operacion == '+':
	resultado = num1 + num2
	print (str(num1) + " + " + str(num2) + " = " + str(resultado))
elif operacion == '-':
	resultado = num1 - num2
	print (str(num1) + " - " + str(num2) + " = " + str(resultado))
elif operacion == '*':
	resultado = num1 * num2
	print (str(num1) + " * " + str(num2) + " = " + str(resultado))	
elif operacion == '/':
	try:
		resultado = num1 / num2
		print (str(num1) + " / " + str(num2) + " = " + str(resultado))
	except ZeroDivisionError:
		print ("Division no valida.")
else:
	print ("Operador incorrecto.")
