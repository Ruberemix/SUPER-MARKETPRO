# 🛒 SuperMarket Pro

Sistema de gestión de inventario para supermercados desarrollado en Python con interfaz gráfica moderna.

## 📋 Descripción

SuperMarket Pro es una aplicación de escritorio que permite administrar el inventario de un supermercado de forma sencilla e intuitiva. Cuenta con un dashboard con estadísticas en tiempo real y un módulo completo de gestión de productos.

## ✨ Características

- 📊 **Dashboard** con tarjetas de estadísticas en tiempo real
  - Total de productos activos
  - Productos con bajo stock
  - Valor total del inventario
  - Total de categorías
- 📦 **Gestión de Inventario**
  - Agregar, editar y eliminar productos
  - Búsqueda por nombre o código
  - Filtro por categoría y bajo stock
  - Ajuste de stock con registro de movimientos
- 🔄 **Historial de movimientos** (entradas y salidas)
- ⚠️ **Alertas de bajo stock** automáticas
- 🎨 Interfaz moderna modo oscuro con CustomTkinter
- 💾 Base de datos local con SQLite

## 🗂️ Categorías incluidas por defecto

Lácteos, Carnes, Frutas y Verduras, Bebidas, Limpieza, Panadería, Enlatados, Congelados

## 🛠️ Tecnologías

| Tecnología | Uso |
|---|---|
| Python 3.13 | Lenguaje principal |
| CustomTkinter | Interfaz gráfica moderna |
| SQLite3 | Base de datos local |
| Pillow | Manejo de imágenes |

## 📦 Instalación

### Requisitos
- Python 3.10+
- pip

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/supermarket-pro.git
cd supermarket-pro

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar
python main.py
```

## 📄 requirements.txt
