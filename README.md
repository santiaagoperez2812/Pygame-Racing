Este es un **README** diseñado para que cualquier persona pueda entender, instalar y jugar tu videojuego. Está estructurado de forma profesional y clara.

---

# 🏎️ No Te Choques

**No Te Choques** es un videojuego arcade desarrollado en Python utilizando la librería **Pygame**. El objetivo es simple pero desafiante: esquivar los vehículos que circulan en ambas direcciones por la carretera mientras intentas obtener el puntaje más alto.

## 📝 Descripción
Tomas el control de un auto azul en una carretera infinita. Deberás tener cuidado, ya que hay camiones ("trocas") que vienen tanto en tu misma dirección como en sentido contrario. El juego termina si colisionas con cualquier obstáculo.

---

## 🚀 Características
* **Movimiento en 8 direcciones:** Libertad total para moverte por la pantalla.
* **Sistema de Colisiones Preciso:** Utiliza `pygame.mask` para detectar choques basados en los píxeles reales de los sprites, no solo en sus rectángulos.
* **Generación Inteligente:** Los enemigos aparecen en posiciones aleatorias y cuentan con un sistema para evitar que se encimen unos sobre otros al aparecer.
* **Interfaz de Usuario:** Incluye menús de inicio y pantallas de "Game Over" con fondos animados.
* **Dificultad Variable:** Los enemigos tienen velocidades aleatorias que cambian cada vez que reaparecen.

---

## 🛠️ Requisitos del Sistema
1.  **Python 3.x** instalado.
2.  **Pygame** instalado. Puedes instalarlo ejecutando:
    ```bash
    pip install pygame
    ```

---

## 📁 Estructura del Proyecto
El código está organizado de forma modular para facilitar su mantenimiento:

* `juego.py`: El núcleo del juego (Game Loop, lógica de estados y pantallas).
* `enemigos.py`: Lógica de comportamiento y movimiento de los obstáculos.
* `sprites.py`: Carga y escalado de imágenes y creación de máscaras de colisión.
* `constantes.py`: Configuración general como colores y dimensiones de la ventana.
* `/sprites`: Carpeta que debe contener los archivos `carro_azul.png`, `troca.png` y `carretera.jpg`.

---

## 🎮 Instrucciones de Juego

### Controles
| Acción | Teclas |
| :--- | :--- |
| **Moverse** | Flechas de dirección o `W`, `A`, `S`, `D` |
| **Iniciar/Reintentar** | Barra Espaciadora (`SPACE`) |
| **Salir** | Tecla `Q` |

### Objetivo
* Esquiva los camiones el mayor tiempo posible.
* Cada segundo que sobrevivas aumentará tu puntuación.
* ¡Supera tu propio récord!

---

## ⚙️ Instalación y Ejecución
1.  Clona o descarga este repositorio.
2.  Asegúrate de tener la carpeta `sprites/` con las imágenes necesarias.
3.  Abre una terminal en la carpeta del proyecto.
4.  Ejecuta el comando:
    ```bash
    python juego.py
    ```

---

## 💡 Notas de Desarrollo
El juego implementa una técnica de **fondo infinito** mediante el uso de dos imágenes de carretera que se desplazan verticalmente y se reposicionan cuando una sale del borde de la pantalla, creando una ilusión de movimiento constante.
