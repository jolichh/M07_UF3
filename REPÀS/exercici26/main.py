'''
Crear un arxiu de nom user.py. En aquest arxiu s’ha de crear una class de nom user. Aquesta class ha de tindre:
    Constructor
    Atributs (mínim 6)
    Getters/Setters
    Mètode de nom salutacio on es mostren, per pantalla, totes les dades (atributs) del user.
    Afegir el mètode to_dict(self) a les dues classes per retornar l’objecte en format json

'''
from user import User
user = User("John", "Doe", 20, "john.doe@example.com", "123456789", "123 Balmes")
user.salutacio()
print(user.to_dict())