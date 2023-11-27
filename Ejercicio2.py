dictClase = {'Ainara' : False,
              'Martin' : True}
while True:
    option = input('Introduzca la opción que desee realizar: \n (1) Añadir alumno/a, \n (2) Número de aprobados, \n (3) Mostrar todo el alumnado \n')


    match option :

        case '1':
            nombre = input('Introduzca el nombre del alumno/a. ')
            nota = bool(input('Introduzca si el alumno ha aprobado (1 / True) o no (0 / False) '))
            dictClase[nombre] = nota
            
        case '2':
            contador = 0

            for alumno in dictClase:
                a = dictClase.get(alumno)
                
                if a == True:
                    contador +=1
            print(f'El número de aprobados es: {contador}')
            
        case '3':
            print(dictClase)
