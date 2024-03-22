#Cree una función lambda con la misma funcionalidad 
#que la función de suma que acaba de crear.
a = 7
b = 23  #definimos los valores de los 3 argumentos
c = 45

suma = lambda a, b, c: a + b + c #asignamos a la función lambda suma los argumentos.
                                 #también indicamos la operación a realizar.
resultado = suma(a, b, c)        #en resultado guardamos el resultado de la función.

print(resultado)                 #Ta Channnn