# Reflexão em torno do eixo dos y

from pylab import*
from plot_vetores import*

def T(x,y):
    return quiver(0,0,-x,y, scale_units='xy', angles='xy', scale=1)

fig = figure(figsize=(10,10))

vetor(2,3) # vetor em azul
T(2,3)

xlim(-5,5)
ylim(-5,5)
grid()
show()
