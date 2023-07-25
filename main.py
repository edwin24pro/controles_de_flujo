import variables_reservadas
import in_datos

lista = []
datos = ''
indice = 0

while len(lista)<5:
    in_lista = input('Escribe palabras: ')
    lista.append(in_lista)

for texto in range(0, len(lista)):
    if lista[texto] == 'disco':
        datos = lista[texto]
        indice = texto

if indice == 0 and datos == '':
    print(f'''
    error
    ''')
else:
    print(f'''
    La palabra disco se encuentra en el indice {indice}
    gracias''')