import json

class User:
    def __init__(self, nom, cognom, edat, correu, telefon, adreca):
        self.nom = nom
        self.cognom = cognom
        self.edat = edat
        self.correu = correu
        self.telefon = telefon
        self.adreca = adreca

    def getNom(self):
        return self.nom
    def getCognom(self):
        return self.cognom
    def getEdat(self):
        return self.edat
    def getCorreu(self):
        return self.correu
    def getTelefon(self):
        return self.telefon
    def getAdreca(self):
        return self.adreca

    def setNom(self, nom):
        self.nom = nom
    def setCognom(self, cognom):
        self.cognom = cognom
    def setEdat(self, edat):
        self.edat = edat
    def set_correu(self, correu):
        self.correu = correu
    def setTelefon(self, telefon):
        self.telefon = telefon
    def setAdreca(self, adreca):
        self.adreca = adreca

    # Mostrar dades
    def salutacio(self):
        print(f"Nom: {self.nom}")
        print(f"Cognom: {self.cognom}")
        print(f"Edat: {self.edat}")
        print(f"Correu: {self.correu}")
        print(f"Telèfon: {self.adreca}")

    # Convertir l'objecte a un diccionari (format json)
    def to_dict(self):
        return {
            "nom": self.nom,
            "cognom": self.cognom,
            "edat": self.edat,
            "correu": self.correu,
            "telefon": self.telefon,
            "adreca": self.adreca
        }