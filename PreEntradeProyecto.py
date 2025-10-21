import os

# Lista de productos con algunos ejemplos
productos = [
    ["Manzana", "Fruta", 100],
    ["Leche", "Lácteo", 250],
    ["Pan", "Panadería", 80]
]

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPresiona Enter para continuar...")

def validar_cadena(mensaje):
    while True:
        entrada = input(mensaje).strip()
        if entrada:
            return entrada
        print("❌ El campo no puede estar vacío. Intenta de nuevo.")

def validar_precio(mensaje):
    while True: 
        entrada = input(mensaje).strip()
        if not entrada:
            print("❌ El precio no puede estar vacío.")
            continue
        try:
            precio = int(entrada)
            if precio >= 0:
                return precio
            else:
                print("❌ El precio debe ser un número positivo o cero.")
        except ValueError:
            print("❌ Entrada incorrecta. Ingresa un número entero para el precio.")

def agregar_producto():
    print("\n--- 🛒 AGREGAR PRODUCTO ---")
    nombre = validar_cadena("Ingresa el nombre del producto: ")
    categoria = validar_cadena("Ingresa la categoría del producto: ")
    precio = validar_precio("Ingresa el precio del producto (sin centavos): $")
    productos.append([nombre, categoria, precio])
    print(f"✅ Producto '{nombre}' agregado con éxito.")
    pausar()

def visualizar_productos():
    print("\n--- 📋 PRODUCTOS REGISTRADOS ---")
    if not productos:
        print("La lista de productos está vacía.")
    else:
        for i, producto in enumerate(productos, 1):
            nombre, categoria, precio = producto
            print(f"{i}. {nombre:<20} | {categoria:<15} | ${precio}")
    pausar()

def buscar_productos():
    print("\n--- 🔎 BUSCAR PRODUCTOS ---")
    termino_busqueda = validar_cadena("Ingresa el nombre del producto a buscar: ").lower()
    resultados = [p for p in productos if termino_busqueda in p[0].lower()]
    if resultados:
        print("\n🎉 Coincidencias encontradas:")
        for nombre, categoria, precio in resultados:
            print(f"- Nombre: {nombre} | Categoría: {categoria} | Precio: ${precio}")
    else:
        print(f"❌ No se encontraron productos con el nombre '{termino_busqueda}'.")
    pausar()

def eliminar_producto():
    print("\n--- 🗑️ ELIMINAR PRODUCTO ---")
    if not productos:
        print("No hay productos para eliminar.")
        pausar()
        return
    visualizar_productos()
    while True:
        posicion_str = input("Ingresa el número del producto a eliminar (o 'c' para cancelar): ").strip().lower()
        if posicion_str == 'c':
            print("Operación cancelada.")
            pausar()
            return
        try:
            posicion = int(posicion_str) - 1
            if 0 <= posicion < len(productos):
                nombre_eliminado = productos.pop(posicion)[0]
                print(f"🗑️ Producto '{nombre_eliminado}' eliminado con éxito.")
                pausar()
                break
            else:
                print("❌ Número de producto inválido. Intenta de nuevo.")
        except ValueError:
            print("❌ Entrada inválida. Ingresa un número o 'c' para cancelar.")

def sistema_gestion_productos():
    while True:
        limpiar_pantalla()
        print("=============================================")
        print("       SISTEMA DE GESTIÓN BÁSICA DE PRODUCTOS")
        print("=============================================")
        print("1. Agregar producto")
        print("2. Visualizar productos") 
        print("3. Buscar producto") 
        print("4. Eliminar producto") 
        print("5. Salir")
        print("---------------------------------------------")
        
        opcion = input("Elige una opción (1-5): ").strip()

        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            visualizar_productos()
        elif opcion == '3':
            buscar_productos()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            print("\n👋 ¡Gracias por usar el Sistema de Gestión! Saliendo del programa...")
            break 
        else:
            print("❌ Opción no válida. Por favor, elige un número del 1 al 5.")
            pausar()

if __name__ == "__main__":
    sistema_gestion_productos()
