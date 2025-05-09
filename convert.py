#!/usr/bin/env python3
import cv2
import sys

# ============ CONFIG ============

if len(sys.argv) < 2:
    print("Uso: python3 convert.py imagen.jpg", file=sys.stderr)
    sys.exit(1)

IMAGE_PATH  = sys.argv[1]
OUTPUT_PATH = 'coordenadas.txt'
RESIZE_W    = 300   # ancho para procesar la imagen en píxeles

# Rango físico de los ejes (grados de motor)
X_MIN, X_MAX = -1400, -200
Y_MIN, Y_MAX =   200, 1800

# ============ CARGA & REDIMENSIÓN ============

img = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)
if img is None:
    print(f"ERROR: no puedo cargar '{IMAGE_PATH}'", file=sys.stderr)
    sys.exit(1)

h0, w0 = img.shape
scale_px = RESIZE_W / float(w0)
w = RESIZE_W
h = int(h0 * scale_px)
img = cv2.resize(img, (w, h), interpolation=cv2.INTER_AREA)

# ============ BINARIZAR & CONTORNOS ============

_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# ============ CÁLCULO DE ESCALA UNIFORME & CENTRADO ============

span_x = X_MAX - X_MIN
span_y = Y_MAX - Y_MIN

# escala única para no deformar:
scale = min(span_x / float(w), span_y / float(h))

# margen sobrante tras escalar:
margin_x = (span_x - w * scale) / 2.0
margin_y = (span_y - h * scale) / 2.0

def map_point(px, py):
    """
    px,py: coordenadas de píxel (0..w-1, 0..h-1).
    Devuelve x,y en grados de motor, centrados y escalados al 50%,
    con volteo horizontal para corregir espejo.
    """
    # Voltear X para corregir “mirrored”
    px = (w - 1) - px

    # convertir píxeles a “grados relativo al rango”
    x = X_MIN + margin_x + px * scale
    # invertimos Y para que py=0 esté en arriba
    y = Y_MIN + margin_y + (h - 1 - py) * scale

    # clamping por si quedase fuera
    x = max(X_MIN, min(X_MAX, x))
    y = max(Y_MIN, min(Y_MAX, y))

    return int(round(x)), int(round(y))

# ============ ESCRIBIR COORDENADAS ============

with open(OUTPUT_PATH, 'w') as f:
    for cnt in contours:
        if len(cnt) < 2:
            continue
        first = True
        for pt in cnt:
            px, py = pt[0]
            x, y = map_point(px, py)
            if first:
                f.write(f"M {x},{y}\n")
                first = False
            else:
                f.write(f"L {x},{y}\n")
        f.write("\n")

print(f"→ Coordenadas generadas en '{OUTPUT_PATH}'")
