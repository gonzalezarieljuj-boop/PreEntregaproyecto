# 📚 Pre-Entrega de Proyecto: Sistema Básico de Gestión de Productos

[cite_start]Este repositorio contiene la solución para la pre-entrega de proyecto del curso [cite: 1, 9][cite_start], que consiste en el diseño e implementación de un sistema básico que permita gestionar información inicial sobre los productos de la empresa[cite: 9].

El proyecto fue desarrollado en **Python** y cumple con todos los requisitos solicitados, enfocándose en un código simple, didáctico y fácil de entender, utilizando estructuras de datos fundamentales y lógica de programación básica (bucles y condicionales).

## 🚀 Requerimientos del Sistema

[cite_start]El programa en Python [cite: 24] debe permitir gestionar la información de productos cumpliendo las siguientes funcionalidades:

* [cite_start]**Ingreso de datos de productos**: El sistema debe permitir ingresar datos básicos de los productos: nombre, categoría, y precio (sin centavos)[cite: 25]. [cite_start]Estos datos deben almacenarse en una lista, donde cada producto sea representado como una sublista de tres elementos (nombre, categoría, y precio)[cite: 26, 28].
* [cite_start]**Visualización de productos registrados**: El programa debe incluir una funcionalidad para mostrar en pantalla todos los productos ingresados[cite: 27]. [cite_start]La información debe presentarse de manera ordenada y legible, con cada producto numerado[cite: 29].
* [cite_start]**Búsqueda de productos**: El sistema debe permitir buscar productos por su nombre[cite: 32]. [cite_start]Si encuentra coincidencias, debe mostrar la información completa de los productos que coincidan[cite: 33]. [cite_start]Si no hay coincidencias, debe informar que no se encontraron resultados[cite: 34].
* [cite_start]**Eliminación de productos**: El sistema debe permitir eliminar un producto de la lista, identificándolo por su posición (número) en la lista[cite: 35].

## ⚙️ Requisitos Técnicos y Metodológicos

| Requisito | Implementación |
| :--- | :--- |
| **Almacenamiento de Datos** | [cite_start]Usar listas para almacenar y gestionar los datos[cite: 39]. |
| **Estructuras de Control** | [cite_start]Incorporar bucles `while` y `for` según corresponda[cite: 39]. |
| **Validaciones** | [cite_start]Validar entradas del usuario o usuaria, asegurándote de que no se ingresen datos vacíos o incorrectos[cite: 40]. |
| **Menú y Opciones** | [cite_start]Presentar un menú que permita elegir entre las funcionalidades disponibles. [cite_start]El programa debe continuar funcionando hasta que se elija una opción para salir[cite: 43]. |
| **Lógica Condicional** | [cite_start]Utilizar condicionales para gestionar las opciones del menú y las validaciones necesarias[cite: 41]. |

## 🚀 Cómo Ejecutar el Proyecto

### 1. Requisitos Previos

Necesitas tener **Python 3** instalado en tu sistema operativo.

### 2. Ejecución

1.  Guarda el código fuente del sistema en un archivo llamado, por ejemplo, `gestion_productos.py`.
2.  Abre la terminal o línea de comandos.
3.  Navega hasta la carpeta donde guardaste el archivo.
4.  Ejecuta el programa con el siguiente comando:

```bash
python gestion_productos.py
