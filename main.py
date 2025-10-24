from Services.Tienda_service import TiendaService
from models.Usuario import Cliente, Administrador
from models.Producto import Producto, Producto_electronico, Producto_ropa

# Crear instancia del servicio
tienda = TiendaService()

# Registrar usuarios
cliente1 = Cliente("Miguel", "miguel@email.com", "36210")
cliente2 = Cliente("Lucía", "lucia@email.com", "36212")
cliente3 = Cliente("Carlos", "carlos@email.com", "36214")
admin = Administrador("Noelia", "noe@gmail.com")

tienda.registrar_usuario(cliente1)
tienda.registrar_usuario(cliente2)
tienda.registrar_usuario(cliente3)
tienda.registrar_usuario(admin)

# Crear productos
p1 = Producto("Libro", 25.00, 10)
p2 = Producto_electronico("Auriculares", 60.00, 5, garantia=12)
p3 = Producto_ropa("Camiseta", 15.00, 20, talla="M", color="Azul")
p4 = Producto_ropa("Sudadera", 35.00, 8, talla="L", color="Negra")
p5 = Producto_electronico("Teclado", 45.00, 6, garantia=24)

# Añadir productos al inventario
tienda.agregar_producto(p1)
tienda.agregar_producto(p2)
tienda.agregar_producto(p3)
tienda.agregar_producto(p4)
tienda.agregar_producto(p5)

# Listar productos
print("\n Productos disponibles:")
tienda.listar_productos()

# Crear pedidos
pedido1 = tienda.crear_pedido(cliente1.id, [(p1, 2), (p2, 1)])
pedido2 = tienda.crear_pedido(cliente2.id, [(p3, 3), (p4, 1)])
pedido3 = tienda.crear_pedido(cliente3.id, [(p5, 2), (p1, 1)])
pedido4 = tienda.crear_pedido(cliente1.id, [(p3, 2), (p5, 1)])

# Mostrar resumen de pedidos
print("\n Pedido de Miguel:")
print(pedido1)

print("\n Pedido de Lucía:")
print(pedido2)

print("\n Pedido de Carlos:")
print(pedido3)

# Mostrar pedidos por cliente
print("\n Pedidos de Miguel ordenados por fecha:")
tienda.listar_pedidos_por_cliente(cliente1.id)

print("\n Productos disponibles:")
tienda.listar_productos()
