#Autor: Cesar Ramirez Hernandez

#Programa que permite calcular el Crc de una cadena de texto
#El Polinomio Usado es ------>  x^5 + x^4 + x^2 + 1 y en binario: "110101" 



def crc(mensaje, polinomio, crc_code = 0): #Función crc

	AuxiliarLista=[]

	if crc_code == 0 : # Si se quiere calcular por 1era vez
		#Se agregan tantos ceros (0) indique el grado del polinomio
		crc_code = ''
		for i in range(len(polinomio) -1):
			crc_code = crc_code + '0'
           
	# Se agrega el crc al mensaje(data).
	mensaje = mensaje + crc_code
	#print(mensaje)

	# Se convierte tanto el mensaje(data) como el generador a listas 
	mensaje = list(mensaje)
	polinomio = list(polinomio)
	#print(mensaje,' ---')
	#print(polinomio,' ...')
	#print(len(mensaje),'-------',len(crc_code))

	# Para i divisiones
	for i in range(len(mensaje) - len(crc_code)):
		if mensaje[i] == '1': # si el bit es un uno (1)
			# Para cada bit del generador
			for j in range(len(polinomio)):
				#Dividir cada bit del generador con el del msg y traer el sgte. 
				mensaje[i+j] = str( ( int(mensaje[i+j]) ^ int(polinomio[j]) ) ) 
                #print('[',i,j,'] ',int(mensaje[i+j]),int(polinomio[j]),mensaje[i+j],mensaje)
				AuxiliarLista=mensaje

			print(''.join(AuxiliarLista))
                                
                                     
	# devolver n bits como se hayan agregado
	return ''.join(mensaje[-len(crc_code):])        

	
cadenaAuxiliar=""
def convertidor(data):
	global cadenaAuxiliar
	
	for x in data:                
		cadenaBinaria = format(ord(x), 'b')                                #convierte letra por letra a binario
		longitud = len(cadenaBinaria)                                      #calcula la longitud de la cadena en binario
                
		if longitud < 8:
			bitFaltantes = 8 - longitud
			for x in range(bitFaltantes):
				cadenaBinaria = '0' + cadenaBinaria
			cadenaAuxiliar = cadenaAuxiliar + cadenaBinaria
                                  
		else:
			cadenaAuxiliar = cadenaAuxiliar + cadenaBinaria                                       
		
	return cadenaAuxiliar


polinomio='110101' # Polinomio Usado ------>  x^5 + x^4 + x^2 + 1 
#polinomio = input('\nIngresa el polinomio en binario: ')

data = input('Ingresar la cadena: ') # Pedimos la cadena para calcular el crc
mensaje_binario = convertidor(data) #convertimos la cadena a binario

print("\n")
crc_code = crc(mensaje_binario,polinomio) # Calculamos el CRC

print("\n")
print("Binario: " ,mensaje_binario)
print("Calculo del crc en binario: " ,crc_code)

#decimal=int(crc_code,2)
#print("Calculo del crc en Hexadecimal: " ,format(decimal, 'X'))

