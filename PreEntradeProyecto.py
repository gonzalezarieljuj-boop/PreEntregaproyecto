# Inicialización de la lista de productos
# Cada producto se almacena como una sublista: [nombre, categoría, precio]
# Requisito: Usar listas para almacenar y gestionar los datos 
productos = []

# --- Funciones Auxiliares ---

def validar_cadena(mensaje):
    """Valida que la entrada del usuario no esté vacía."""
    while True: # Requisito: Incorporar bucles while 
        entrada = input(mensaje).strip()
        if entrada: # Requisito: Validar entradas del usuario, asegurándote de que no se ingresen datos vacíos 
            return entrada
        else:
            print("❌ El campo no puede estar vacío. Intenta de nuevo.")

def validar_precio(mensaje):
    """Valida que el precio ingresado sea un número entero positivo."""
    while True: # Requisito: Incorporar bucles while 
        entrada = input(mensaje).strip()
        if not entrada:
            print("❌ El precio no puede estar vacío.")
            continue
        try:
            # Requisito: Precio sin centavos (entero) [cite: 25]
            precio = int(entrada)
            if precio >= 0:
                return precio
            else:
                print("❌ El precio debe ser un número positivo o cero.")
        except ValueError:
            # Requisito: Validar entradas, asegurándote de que no se ingresen datos incorrectos 
            print("❌ Entrada incorrecta. Ingresa un número entero para el precio.")


# --- Funcionalidades del Sistema ---

def agregar_producto():
    """Permite ingresar un nuevo producto a la lista."""
    print("\n--- 🛒 AGREGAR PRODUCTO ---")
    
    # Requisito: Ingreso de datos básicos (nombre, categoría, precio sin centavos) [cite: 25]
    nombre = validar_cadena("Ingresa el nombre del producto: ")
    categoria = validar_cadena("Ingresa la categoría del producto: ")
    precio = validar_precio("Ingresa el precio del producto (sin centavos): $")
    
    # Requisito: Almacenar como sublista de tres elementos 
    nuevo_producto = [nombre, categoria, precio]
    productos.append(nuevo_producto)
    print(f"✅ Producto '{nombre}' agregado con éxito.")

def visualizar_productos():
    """Muestra todos los productos registrados en la lista."""
    print("\n--- 📋 PRODUCTOS REGISTRADOS ---")
    if not productos: # Requisito: Usar condicionales 
        print("La lista de productos está vacía.")
        return

    # Requisito: Información presentada de manera ordenada y legible, con cada producto numerado 
    for i in range(len(productos)): # Requisito: Incorporar bucles for 
        # El número de posición es i + 1, ya que las listas empiezan en 0
        nombre, categoria, precio = productos[i] 
        print(f"{i + 1}. Nombre: {nombre} | Categoría: {categoria} | Precio: ${precio}")

def buscar_productos():
    """Permite buscar productos por su nombre."""
    print("\n--- 🔎 BUSCAR PRODUCTOS ---")
    termino_busqueda = validar_cadena("Ingresa el nombre del producto a buscar: ").lower()
    
    resultados = []
    # Requisito: Usar bucles for para recorrer la lista 
    for producto in productos:
        # El nombre del producto está en el índice 0 de la sublista
        nombre_producto = producto[0].lower()
        if termino_busqueda in nombre_producto: # Requisito: Si encuentra coincidencias [cite: 33]
            resultados.append(producto)

    # Requisito: Usar condicionales para gestionar resultados 
    if resultados:
        print("\n🎉 Coincidencias encontradas:")
        for nombre, categoria, precio in resultados:
            print(f"- Nombre: {nombre} | Categoría: {categoria} | Precio: ${precio}")
    else:
        # Requisito: Si no hay coincidencias, informar que no se encontraron resultados [cite: 34]
        print(f"❌ No se encontraron productos con el nombre '{termino_busqueda}'.")

def eliminar_producto():
    """Permite eliminar un producto por su número de posición."""
    print("\n--- 🗑️ ELIMINAR PRODUCTO ---")
    if not productos:
        print("No hay productos para eliminar.")
        return

    visualizar_productos() # Muestra la lista para que el usuario elija el número
    
    while True: # Requisito: Incorporar bucles while 
        posicion_str = input("Ingresa el número (posición) del producto a eliminar (o 'c' para cancelar): ").strip().lower()
        
        if posicion_str == 'c':
            print("Operación cancelada.")
            return

        try:
            # Requisito: Eliminar un producto identificándolo por su posición (número) en la lista 
            posicion = int(posicion_str) - 1 # Se resta 1 porque la lista es base 0
            
            # Requisito: Validar entradas (que la posición exista) [cite: 40, 41]
            if 0 <= posicion < len(productos): 
                nombre_eliminado = productos[posicion][0]
                productos.pop(posicion) # Elimina el elemento en esa posición
                print(f"🗑️ Producto '{nombre_eliminado}' eliminado con éxito.")
                break
            else:
                print("❌ Número de producto inválido. Intenta de nuevo.")
        except ValueError:
            print("❌ Entrada inválida. Ingresa un número o 'c' para cancelar.")

# --- Función Principal (Menú) ---

def sistema_gestion_productos():
    """Función principal que ejecuta el menú interactivo."""
    # Requisito: El programa debe continuar funcionando hasta que se elija una opción para salir 
    while True: # Bucle principal del programa
        print("\n=============================================")
        # Requisito: Presentar un menú que permita elegir entre las funcionalidades disponibles [cite: 42]
        print("       SISTEMA DE GESTIÓN BÁSICA DE PRODUCTOS")
        print("=============================================")
        print("1. Agregar producto") # Requisito: Agregar productos [cite: 42, 52]
        print("2. Visualizar productos") # Requisito: Visualizar productos [cite: 42, 53]
        print("3. Buscar producto") # Requisito: Buscar productos [cite: 42, 54]
        print("4. Eliminar producto") # Requisito: Eliminar productos [cite: 42, 55]
        print("5. Salir") # Requisito: Opción para salir [cite: 56]
        print("---------------------------------------------")
        
        opcion = input("Elige una opción (1-5): ").strip()

        # Requisito: Utilizar condicionales para gestionar las opciones del menú 
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
            break # Sale del bucle 'while True' principal
        else:
            print("❌ Opción no válida. Por favor, elige un número del 1 al 5.")

# Ejecutar el sistema
if __name__ == "__main__":
    sistema_gestion_productos()