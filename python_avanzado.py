from datetime import datetime

class Plato:
    def __init__ (Self, nombre, precio, ingredientes, tipo):
        self.nombre = nombre
        self.precio = precio
        self.ingredientes = ingredientes
        self.tipo = tipo

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}"
    
class Cliente:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.__email = email
        self.__puntos = 0
        self.__historial = []

    def obtener_email(self):
        return self.__email
    
    def obtener_puntos(self):
        return self.__puntos
    
    def agregar_pedido(self, pedido):
        self.__historial.append(pedido)
        self.__puntos += int(pedido.obtener_total() / 10)

    def canjear_descuento(self):
        if self.__puntos >= 100:
            self.__puntos -= 100
            return 0.15
        elif self.__puntos >= 50:
            self.__puntos -= 50
            return 0.10
        return 0
    
    def __str__(self):
        return f"Cliente: {self.nombre} - Puntos: {self.__puntos}"
    
class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.__estado = "libre"
        self.__cliente = None
        self.__hora = None

    def obtener_estado(self):
        return self.__estado
    
    def esta_disponible(self):
        return self.__estado == "libre"
    
    def ocupar(self, cliente):
        if self.__estado == "libre":
            self.__estado = "ocupada"
            self.__cliente = cliente
            self.__hora = datetime.now()
            return True
        return False
    
    def liberar(self):
        self.__estado = "libre"
        self.__cliente = None
        return datetime.now() - self.__hora if self.__hora else None
    
    def reservar(self):
        it self.__estado == "libre": # type: ignore
            self.__estado = "reservada"
            return True
        return False
    
        def __str__(self):
            return f"Mesa {self.numero} - Cap: {self.capacidad} - {self.__estado}"
    
    

        
