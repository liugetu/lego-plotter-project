#!/usr/bin/env python3
import turtle
import time

# ============ CONFIGURACIÓN DE PLOTTER ============
X_MIN, X_MAX = -1600,   0
Y_MIN, Y_MAX =    0, 2000

UMBRAL_MOVIMIENTO = 10

# ============ SETUP DE TURTLE ============
screen = turtle.Screen()
screen.title("Simulación de exec.py")
# Definimos el sistema de coordenadas para que coincida con el EV3:
screen.setworldcoordinates(X_MIN, Y_MIN, X_MAX, Y_MAX)
screen.bgcolor("white")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)      # máxima velocidad
pen.pensize(2)

# ============ FUNCIONES SIMULADAS ============
estado_lapiz = 'abajo'
last_x, last_y = 0, 0

def subir_lapiz():
    global estado_lapiz
    if estado_lapiz != 'arriba':
        # simulamos la elevación sin mover el Turtle
        estado_lapiz = 'arriba'
    # en simulación no hay acción gráfica
    print("🖋️ Lápiz arriba")

def bajar_lapiz():
    global estado_lapiz
    if estado_lapiz != 'abajo':
        estado_lapiz = 'abajo'
    # en simulación no hay acción extra
    print("🖋️ Lápiz abajo")

def move_xy(dx, dy):
    """Simula el move_xy de EV3 con Turtle, dibujando o no según estado_lapiz."""
    global last_x, last_y

    target_x = last_x + dx
    target_y = last_y + dy

    # Si el lápiz está abajo, trazamos línea; si arriba, movemos sin dibujar
    if estado_lapiz == 'abajo':
        pen.pendown()
    else:
        pen.penup()

    pen.goto(target_x, target_y)

    print(f"→ Sim move to ({target_x}, {target_y}) [{ 'draw' if estado_lapiz=='abajo' else 'move' }]")
    last_x, last_y = target_x, target_y

# ============ LECTURA DE COORDENADAS ============
def leer_coordenadas(path):
    cmds = []
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            cmd, coord = line.split()
            x_str, y_str = coord.split(',')
            cmds.append((cmd, int(x_str), int(y_str)))
    return cmds

# ============ SECUENCIA PRINCIPAL ============
cmds = leer_coordenadas('coordenadas.txt')

# Inicializamos turtle en el origen EV3
pen.penup()
pen.goto(0, 0)
last_x, last_y = 0, 0

for cmd, x, y in cmds:
    # Clampear (por si acaso)
    x = max(X_MIN, min(X_MAX, x))
    y = max(Y_MIN, min(Y_MAX, y))

    print(f"Comando {cmd} → destino ({x},{y})")

    dx = x - last_x
    dy = y - last_y

    if abs(dx) < UMBRAL_MOVIMIENTO and abs(dy) < UMBRAL_MOVIMIENTO:
        print("  ↳ Paso ignorado (demasiado pequeño).")
        continue

    if cmd == 'M':
        subir_lapiz()
    elif cmd == 'L':
        bajar_lapiz()
    else:
        print("❗ Comando desconocido:", cmd)
        continue

    move_xy(dx, dy)

# Al final, levantamos lápiz y volvemos al origen (opcional)
subir_lapiz()
pen.penup()
pen.goto(0, 0)
print("✅ Simulación completada")
turtle.done()
