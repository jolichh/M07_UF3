'''
Buscar error/s en el següent programa. 
Aquest programa elimina el contacte (nom i telèfon) segons el nom passat per paràmetre.

'''
#El problema es que busca eliminar un contacte que no existeix al diccionari
#L'error que ens sortira per consola es KeyError
#Només cal gestionar l'error i guardar el valor per printejar
contactes = {'Roger':678232311, 'Oriol':566879326}

def elimina(contactes, user):
    try:
        eliminar = contactes[user]
        del contactes[user]    
        return "Eliminat: ",eliminar    
    except Exception as e:
        print("ERROR en la busqueda:", e)
        

print(elimina(contactes, 'Sergi'))
