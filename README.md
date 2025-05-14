# Lego Plotter Project
A plotter robot built with Lego.

[Build instructions (PDF / 44MB)](https://jander.me.uk/LEGO/resources/Plott3r.pdf)

Based on a work at http://jander.me.uk/LEGO/plott3r.html.

[Set up to use Python with the Lego brick](https://education.lego.com/en-us/product-resources/mindstorms-ev3/teacher-resources/python-for-ev3/)

# Instructions
To send the image and generate the coordinates (enter the name of the image you want to draw, it should be in the same directory):

<pre><code>python3 convert.py cara1.jpg</code></pre>

This will generate a file `coordenadas.txt` containing the drawing coordinates.

To preview what will be drawn (it will be deformed because it doesn't have the same aspect ratio as the paper):
<pre><code>python3 preview.py</code></pre>

To send the files to the robot (change the IP address to yours):
<pre><code>scp exec4.py coordenadas.txt stop.py robot@169.254.206.221:/home/robot/</code></pre>

The default password to access the robot is `maker`.

To enter the robot and start drawing (I recommend using a different terminal):
<pre><code>ssh robot@169.254.206.221
python3 exec4.py</code></pre>

To exit this mode, just enter `exit`.

In case it doesn't work well and can't stop, or you want to level up the pen:
<pre><code></code>python3 stop.py</code></pre>

Note: a white paper should be used, otherwise, the color sensor might not work well.
