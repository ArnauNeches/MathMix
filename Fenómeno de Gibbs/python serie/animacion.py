import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button
import signo

fig, ax = plt.subplots()
ax.set_xlim(-math.pi, math.pi)
ax.set_ylim(-1.5, 1.5)

x_signo = np.linspace(-math.pi,math.pi,50000)
y_signo = signo.signo(x_signo)
static_line, = ax.plot(x_signo, y_signo, lw=0.7, color='black')

line, = ax.plot([],[],lw=1,color='red')

frame_text = ax.text(0.1, 0.9, '', transform=ax.transAxes, color='black', fontsize=10)

def animate(n):
    x = np.linspace(-math.pi,math.pi,100000)
    y = signo.serie(x, n)
    line.set_data(x,y)

    frame_text.set_text(f'n= {2*n}')

    return line, frame_text

anim = FuncAnimation(fig, animate, frames = 50, interval = 70, blit = True)

plt.title('Suma parcial hasta n=100')

#anim.save('fourier2.gif', writer='pillow', fps=20)

plt.show()
