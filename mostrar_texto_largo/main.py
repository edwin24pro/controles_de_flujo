frutas = []

while len(frutas) < 5:
	nueva_fruta = input('Escribe unas frutas: ')
	for fruta in frutas:
		if len(nueva_fruta) == len(fruta):
			print('misma longitud gil ingresa otro')
	if nueva_fruta in frutas:
		print('ya existe la fruta ecrita ingresa otro')
	else:
		frutas.append(nueva_fruta)

print(frutas)

def texto_largo(frutas):
	longitud_texto = 0
	mostrar_fruta = ''
	for index in range(0,len(frutas)):
		if len(frutas[index]) > longitud_texto:
			longitud_texto = len(frutas[index])
			mostrar_fruta = frutas[index]
			indice = index
			mensaje = f'la palabra {mostrar_fruta} se encuentra en el indice {indice} longitud {longitud_texto}'
	return mensaje
	
print(texto_largo(frutas))