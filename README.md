# Lego Plotter Project
A plotter robot built with Lego that draws images on paper.

<p align="left">
  <img src="https://github.com/user-attachments/assets/7a65e284-3eb8-4691-8e93-a270485fcf3d" width="400"/>
  <img src="https://github.com/user-attachments/assets/8e8efb2e-de8e-415d-87b7-301aa758e72e" width="400"/>
</p>

Hardware design based on http://jander.me.uk/LEGO/plott3r.html.

[Build instructions (PDF / 44MB)](https://jander.me.uk/LEGO/resources/Plott3r.pdf)

[Set up to use Python with the Lego brick](https://education.lego.com/en-us/product-resources/mindstorms-ev3/teacher-resources/python-for-ev3/)

## Instructions
To send the image and generate the coordinates:

<pre><code>python3 convert.py cara1.jpg</code></pre>

This will generate a file `coordenadas.txt` containing the drawing coordinates.

To preview what will be drawn (it will be deformed because it doesn't have the same aspect ratio as the paper (not fixed)):
<pre><code>python3 preview.py</code></pre>

To send the files to the robot (change the IP address to yours):
<pre><code>scp exec4.py coordenadas.txt stop.py robot@169.254.206.221:/home/robot/</code></pre>

The default password to access the robot is `maker`.

To enter the robot and start drawing (I recommend using a different terminal):
<pre><code>ssh robot@169.254.206.221
python3 exec4.py</code></pre>

To exit this mode, just enter `exit`.

<img width="20" height="20" alt="image" src="https://github.com/user-attachments/assets/8e74a0ad-b5b3-4745-998e-9bfadba9f738" />
In case it doesn't work well and can't stop, or you want to level up the pen:
<pre><code></code>python3 stop.py</code></pre>

Note: a white paper should be used, otherwise, the color sensor might not work well.

## Gallery
<p align="left">
  <img src="https://github.com/user-attachments/assets/97185f6e-24ad-48b8-a325-f460522c3112" width="600"/>
</p>

[Video](https://github.com/user-attachments/assets/a6826d78-1466-459e-b019-b41c4170702b)

## Oops moment
When the robot decided to do its own thing: 

<p align="left">
  <img src="https://github.com/user-attachments/assets/02e6cdd5-be72-44a7-be82-42b166191075" width="600"/>
</p>


