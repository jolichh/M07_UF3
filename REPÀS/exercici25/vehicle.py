import json

class Vehicle:
    #constructor
    def __init__(self, marca, model, any_fabricacio, color, num_puerta, num_rueda):
        self.marca = marca
        self.model = model
        self.any_fabricacio = any_fabricacio
        self.color = color
        self.num_puerta = num_puerta
        self.num_rueda = num_rueda

    def get_marca(self):
        return self.marca
    def get_model(self):
        return self.model
    def get_any_fabricacio(self):
        return self.any_fabricacio
    def get_color(self):
        return self.color
    def get_num_puerta(self):
        return self.num_puerta
    def get_num_rueda(self):
        return self.num_rueda
    
    def set_marca(self, marca):
        self.marca = marca
    def set_model(self, model):
        self.model = model
    def set_any_fabricacio(self, any_fabricacio):
        self.any_fabricacio = any_fabricacio
    def set_color(self, color):
        self.color = color
    def set_num_puerta(self, num_puerta):
        self.num_puerta = num_puerta
    def set_num_rueda(self, num_rueda):
        self.num_rueda = num_rueda

    def nom_parts(self):
        print(f"Marca: {self.marca}")
        print(f"Model: {self.model}")
        print(f"Any de fabricació: {self.any_fabricacio}")
        print(f"Color: {self.color}")
        print(f"Numero de portes: {self.num_puerta}")
        print(f"Numero de rodes: {self.num_rueda}")

    def to_dict(self):
        return {
            "marca": self.marca,
            "model": self.model,
            "any_fabricacio": self.any_fabricacio,
            "color": self.color,
            "num_puerta": self.num_puerta,
            "num_rueda": self.num_rueda
        }