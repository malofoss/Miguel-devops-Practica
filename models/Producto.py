import uuid

class Producto:
    def __init__(self, nombre, precio, stock):
        self.id = uuid.uuid4()
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def consultar_stock(self):
        return self.stock

    def actualizar_stock(self, cantidad):
        if cantidad < 0 and abs(cantidad) > self.stock:
            print("No hay suficiente stock para reducir.")
        self.stock += cantidad

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio:.2f}, Stock: {self.stock}, ID: {self.id}"


class Producto_electronico(Producto):
    def __init__(self, nombre, precio, stock, garantia):
        super().__init__(nombre, precio, stock)
        self.garantia = garantia  # en meses

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}, Garantía: {self.garantia} meses, ID: {self.id}"


class Producto_ropa(Producto):
    def __init__(self, nombre, precio, stock, talla, color):
        super().__init__(nombre, precio, stock)
        self.talla = talla
        self.color = color

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}, Talla: {self.talla}, Color: {self.color}, ID: {self.id}"
