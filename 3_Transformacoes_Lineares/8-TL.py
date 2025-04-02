# Dilatação a direção do vetor

from pylab import*
from plot_vetores import*

# Seja T(x,y) = a*(x,y), aqui escolhendo a = 2

def T(x,y):
    return quiver(0,0,2*x,2*y, scale_units='xy', angles='xy', scale=1)

fig = figure(figsize=(10,10))
vetor(1,2)
T(1,2)

xlim(-5,5)
ylim(-5,5)
grid()
show()