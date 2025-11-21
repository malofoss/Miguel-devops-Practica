# PRACTICA 02 - Tienda
### Miguel Ángel Lorenzo Fossati
La práctica consiste en diseñar en Python un sistema básico de tienda online con clases para productos, usuarios y pedidos. Se debe crear una clase Producto con id automático, nombre, precio, stock y métodos para gestión de inventario, además de dos subclases (ProductoElectronico y ProductoRopa). También se implementará la clase Usuario con sus subclases Cliente y Administrador. La clase Pedido deberá asociarse a un cliente, incluir productos con cantidades, calcular el total y generar un resumen. Todo se gestionará mediante una capa de servicios TiendaService, encargada de registrar usuarios, añadir/eliminar productos, crear pedidos verificando stock y listar pedidos por usuario. Finalmente, en main.py se probará el sistema creando usuarios, productos, pedidos y mostrando los resultados por consola.

## Docker

- Dockerfile
- requirements.txt
- README.md
- comando para construir docker build . -t tienda_online
- comando para ejecutar docker run -t tienda_online