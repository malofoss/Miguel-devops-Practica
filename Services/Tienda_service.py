from models.Usuario import Cliente, Administrador, Usuario
from models.Producto import Producto, Producto_electronico, Producto_ropa
from models.Pedido import Pedido

def obtener_fecha(pedido):
    return pedido.fecha

class TiendaService:
    def __init__(self):
        self.usuarios = []         # lista de clientes y administradores
        self.productos = []        # lista de productos
        self.pedidos = []          # lista de pedidos

    #  Registrar usuario
    def registrar_usuario(self, usuario: Usuario):
        self.usuarios.append(usuario)

    #  Añadir producto
    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    #  Eliminar producto por ID
    def eliminar_producto(self, producto= Producto):
        self.productos = [p for p in self.productos if str(p.id) != str(producto.id)]

    #  Listar productos
    def listar_productos(self):
        for producto in self.productos:
            print(producto)

    #  Crear pedido
    def crear_pedido(self, cliente_id, lista_productos, producto= Producto, pedido= Pedido):
        cliente = next((u for u in self.usuarios if str(u.id) == str(cliente_id) and isinstance(u, Cliente)), None)
        if not cliente:
            print("Cliente no encontrado.")
            return None

        pedido = Pedido(cliente)
        for producto, cantidad in lista_productos:
            if producto.stock >= cantidad:
                producto.actualizar_stock(-cantidad)
                pedido.lista_productos.append((producto, cantidad))
            else:
                print(f"No hay suficiente stock de {producto.nombre}. Stock disponible: {producto.stock}")
        self.pedidos.append(pedido)
        return pedido

    #  Listar pedidos por cliente
    def listar_pedidos_por_cliente(self, cliente_id):
        pedidos_cliente = [i for i in self.pedidos if str(i.cliente.id) == str(cliente_id)]
        pedidos_ordenados = sorted(pedidos_cliente, key=obtener_fecha)
        for pedido in pedidos_ordenados:
            print(pedido)
