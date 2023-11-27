def OrdenarNombres(nombreCompleto):
    """Función que recibe un 'nombre y apellido' y devuelve el 'apellido, nombre'.

        Parámetro: 
        - nombreCompleto = cadena en formato 'Nombre Apellido'.
        Salida:
        - nuevoNombre = cadena en el formato'Apellido, Nombre'.   
    
    """
    nombre, apellido = nombreCompleto.split(' ')
    nuevoNombre = str(apellido.title() +', '+ nombre.title())
    
    print(nuevoNombre)
    return






def ListaNombres(lista, nombreCompleto):
    """Función que recibe una lista de nombres y la ordena por apellidos en orden alfabético.
    
        Parámetro:  -   lista = Lista de nombres que guarda una cantidad indeterminada de nombres
                            con el siguiente formato:
                            ['Nombre Apellido 1', 'Nombre Apellido 2', ...,'Nombre Apellido N']
                    - nombreCompleto = cadena en formato 'Nombre Apellido'.
        
        Salida: newList = Lista de nombres ordenados alfabéticamente en este formato:
                            ['Apellido, Nombre 1', 'Apellido, Nombre 2', ..., 'Apellido, Nombre N',]
    
    """
    newList = []
    for nombre in lista:
        print(OrdenarNombres(nombreCompleto))
        OrdenarNombres(nombre)
        newList.append(nombre)
        

    return print(newList)






ListaNombres(['Ainara Cabrera', 'Martin Cabrera', 'AAA AAA'])