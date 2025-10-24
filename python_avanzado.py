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
    
class Pedido:
    contador = 0

    def __init__(self, cliente, mesa):
        Pedido.contador += 1
        self.numero = Pedido.contador
        self.cliente = cliente
        self.mesa = mesa
        self.__platos = []
        self.__estado = "nuevo"
        self.__subtotal = 0.0
        self.__descuento = 0.0
        self.__propina = 0.0

    def agregar_plato(self, plato, cantidad=1):
        if self.__estado in ["nuevo", "en_preparacion"]:
            self.__platos.extend([plato] * cantidad)
            self.__subtotal = sum(p.precio for p in self.__platos)
            return True
        return False
    
    def enviar_cocina(self, inventario):
        if self.__estado == "nuevo" and self.__platos:
            if all(inventario.verificar(p.ingredientes) for p in self.__platos):
                self.__estado = "en preparacion"
                for p in self.__platos:
                    inventario.descontar(p.ingredientes)
                print(f"Pedido #{self.numero} en cocina")
                return True
            return False
        
    def marcar_listo(self):
        if self.__estado == "en_preparacion":
            self.__estado = "listo"

    def servir(self):
        if self.__estado == "listo":
            self.__estado = "servido"

    def pagar(self, propina=0.0):
        if self.__estado == "servido":
            self.__propina = propina
            self.__estado = "pagado"
            self.cliente.agregar_pedido(self)
            return self.__subtotal - self.__descuento + self.__propina
        return 0
    
    def aplicar_descuento(self, porcentaje):
        if 0 <= porcentaje <= 50:
            self.__descuento = self.__subtotal * (porcentaje / 100)
            return True
        return False
    
    def obtener_total(self):
        return self.__subtotal - self.__descuento + self.__propina
    
    def ticket(self):
        t = f"\n{'='*40}\n SABORES DEL MUNDO\n{'='*40}\n"
        t += f"Pedido #{self.numero} - Mesa {self.mesa.numero}\n"
        t += f"Cliente: {self.cliente.nombre}\n{'='*40}\n"
        for i, p in enumerate(self.__platos, 1):
            t += f"{i}. {p.nombre} ${p.precio:.2f}\n"
        t += f"{'='*40}\n"
        t += f"Subtotal: ${self.__subtotal:.2f}\n"
        if self.__descuento > 0:
            t += f"Descuento: -${self.__descuento:.2f}\n"
        if self.__propina > 0:
            t += f"Propina: ${self.propina:.2f}\n"
        t += f"{'='*40}\nTOTAL: ${self.obtener_total():.2f}\n{'='*40}\n"
        return t
    
class Reserva:
    def __init__(self, cliente, fecha, hora, personas):
        self.cliente = cliente
        self.fecha = fecha
        self.hora = hora
        self.personas = personas
        self.__mesa = None
        self.__estado = "pendiente"

    def realizar(self, sistema):
        mesa = sistema.buscar_mesa(self.personas)
        if mesa:
            mesa.reservar()
            self.__mesa = mesa
            self.__estado = "confirmada"
            print(f"Reserva OK - Mesa {mesa.numero}")
            return True
        print("Sin mesas disponibles")
        return False
    
    def cancelar(self):
        if self.__mesa and self.__estado == "confirmada":
            self.__mesa.liberar()
            self.__estado = "cancelada"




        
