#Utilizando la siguiente lista y variable, 
#determine si el valor de la variable coincide o no con un valor de la lista.

nombre = 'Enrique'

lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

for coincidencia in lista_nombre: #Recorremos con el condicional lista_nombre
    if coincidencia == nombre:    #Si algun argumento coincide con Enrique 
        print(f"{nombre} está en la lista!" ) #imprimirá la veracidad de la coincidencia
        break   #finalizamos en caso de coincidencia, pues de lo contrario ejecutaría el else también.

else:
    print(f"{nombre} no está en la lista!") #si nombre no está incluido en los argumentos de lista_nobmre,
                                            #nos mostrará este mensaje.
    