# 📚 Pre-Entrega de Proyecto: Sistema Básico de Gestión de Productos

Este repositorio contiene la solución para la pre-entrega de proyecto del curso, que consiste en el diseño e implementación de un sistema que permita gestionar información inicial sobre los productos de la empresa.

El proyecto fue desarrollado en **Python** y cumple con todos los requisitos solicitados, enfocándose en un código simple, didáctico y fácil de entender, utilizando estructuras de datos fundamentales y lógica de programación básica (bucles y condicionales).

## 🚀 Requerimientos del Sistema

El programa en Python debe permitir gestionar la información de productos cumpliendo las siguientes funcionalidades:

* Ingreso de datos de productos**: El sistema debe permitir ingresar datos básicos de los productos: nombre, categoría, y precio (sin centavos) Estos datos deben almacenarse en una lista, donde cada producto sea representado como una sublista de tres elementos (nombre, categoría, y precio).
* Visualización de productos registrados**: El programa debe incluir una funcionalidad para mostrar en pantalla todos los productos ingresados. La información debe presentarse de manera ordenada y legible, con cada producto numerado.
* Búsqueda de productos**: El sistema debe permitir buscar productos por su nombre. Si encuentra coincidencias, debe mostrar la información completa de los productos que coincidan. Si no hay coincidencias, debe informar que no se encontraron resultados.
* Eliminación de productos**: El sistema debe permitir eliminar un producto de la lista, identificándolo por su posición (número) en la lista.

## ⚙️ Requisitos Técnicos y Metodológicos

| Requisito | Implementación |
| :--- | :--- |
| **Almacenamiento de Datos** | Usar listas para almacenar y gestionar los datos. |
| **Estructuras de Control** | Incorporar bucles `while` y `for` según corresponda. |
| **Validaciones** | Validar entradas del usuario o usuaria, asegurándote de que no se ingresen datos vacíos o incorrectos. |
| **Menú y Opciones** | Presentar un menú que permita elegir entre las funcionalidades disponibles. El programa debe continuar funcionando hasta que se elija una opción para salir. |
| **Lógica Condicional** | Utilizar condicionales para gestionar las opciones del menú y las validaciones necesarias. |

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
