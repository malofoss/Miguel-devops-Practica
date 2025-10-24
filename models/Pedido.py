import uuid
from datetime import datetime
from models.Usuario import Cliente
from models.Producto import Producto

class Pedido:
    def __init__(self, cliente: Cliente):
        self.id = uuid.uuid4()
        self.fecha = datetime.now()
        self.cliente = cliente  # instancia de Cliente
        self.lista_productos = []  # lista de tuplas: (producto, cantidad)

    def calcular_total(self, producto= Producto):
        total = 0
        for producto, cantidad in self.lista_productos:
            total += producto.precio * cantidad
        return total

    def __str__(self, producto= Producto):
        resumen_productos = "\n".join(
            [f"- {producto.nombre} x{cantidad} = {producto.precio * cantidad:.2f}€"
             for producto, cantidad in self.lista_productos]
        )
        return (
            f"Pedido ID: {self.id}\n"
            f"Fecha: {self.fecha.strftime('%d/%m/%Y %H:%M')}\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Productos:\n{resumen_productos}\n"
            f"Total: {self.calcular_total():.2f}€")