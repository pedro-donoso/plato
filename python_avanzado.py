from datetime import datetime

class Plato:
    def __init__ (Self, nombre, precio, ingredientes, tipo):
        self.nombre = nombre
        self.precio = precio
        self.ingredientes = ingredientes
        self.tipo = tipo

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}"