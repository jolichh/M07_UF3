'''
Crear un arxiu de nom vehicle.py. En aquest arxiu s’ha de crear una class de nom vehicle. Aquesta class ha de tindre:
    Constructor
    Atributs (mínim 6)
    Getters/Setters
    Mètode de nom parts on es mostren, per pantalla, totes les dades (atributs) del vehicle.
    Afegir el mètode to_dict(self) a les dues classes per retornar l’objecte en format json
'''
from vehicle import Vehicle
vehicle = Vehicle("Toyota", "Camry", 2020, "Vermell", 4, 4)
vehicle.nom_parts()
print(vehicle.to_dict())