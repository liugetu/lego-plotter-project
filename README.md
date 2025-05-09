# lego-plotter-project
A plotter robot built with Lego

Para enviar la imagen y generar las coordenadas:
# python3 convert.py imagen.jpg

Para ver lo que dibujará 
(saldrá deformado porque no tiene la misma proporción que la hoja)
# python3 preview.py

Para enviárselo al robot:
# scp exec4.py coordenadas.txt stop.py robot@169.254.206.221:/home/robot/

Password: maker

Para entrar al robot y ejecutar:
# ssh robot@169.254.206.221
# python3 exec4.py

Por si deja de funcionar bien o para subir el lápiz:
# python3 stop.py

Nota: se tiene que usar una hoja blanca, no puede ser oscura para el correcto
funcionamiento del sensor de color
