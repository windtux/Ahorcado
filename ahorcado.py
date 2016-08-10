palabra = ['h','o','l','a']
letra1 =input('Bienvenid@s a esta versión muy temprana del juego adivinar la palabra, se le solicitará 4 letras la cual compone nuestra palabra que esta relacionada con un saludo, suerte! introduzca una letra ')
while letra1 != 'h':
    print ('letra o caracter incorrecto')
    letra1 = input('introduzca nuevamente una letra ')
if letra1=='h':
    print ('correcto')
    letra2 = input('introduzca otra letra ')
while letra2 != 'o':
    print ('letra o caracter incorrecto')
    letra2 = input('introduzca nuevamente una letra ')
if letra2 == 'o':
    print ('correcto')
    letra3 = input('introduzca otra letra ')
while letra3 != 'l':
    print ('letra o caracter incorrecto')
    letra3 = input('introduzca nuevamente una letra ')
if letra3 == 'l':
    print ('correcto')
    letra4 = input('introduzca otra letra ')
while letra4 != 'a':
    print ('letra o caracter incorrecto')
    letra4 = input('introduzca nuevamente una letra ')
if letra4 == 'a':
    print ('Correcto!, has acertado finalmente. La palabra es hola')
