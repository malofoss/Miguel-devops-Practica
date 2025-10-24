import uuid

class Usuario:
    def __init__(self, nombre, correo):
        self.id = uuid.uuid4()
        self.nombre = nombre
        self.correo = correo

    def is_admin(self):
        return False

    def __str__(self):
        return f"Usuario: {self.nombre}, Correo: {self.correo}, ID: {self.id}"


class Cliente(Usuario):
    def __init__(self, nombre, correo, direccion_postal):
        super().__init__(nombre, correo)
        self.direccion_postal = direccion_postal

    def __str__(self):
        return f"Cliente: {self.nombre}, Correo: {self.correo}, Dirección: {self.direccion_postal}, ID: {self.id}"


class Administrador(Usuario):
    def __init__(self, nombre, correo):
        super().__init__(nombre, correo)

    def is_admin(self):
        return True

    def __str__(self):
        return f"Administrador: {self.nombre}, Correo: {self.correo}, ID: {self.id}"