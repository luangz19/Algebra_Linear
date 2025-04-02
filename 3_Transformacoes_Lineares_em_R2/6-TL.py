# Reflexão em torno da reta y = x

from pylab import*
from plot_vetores import*
from numpy import*

# Definindo a reta
def f(x):
    return x

# Gráfico da reta
x = linspace(-5,5,50)
y = f(x)


# Definindo a transformação

def T(x,y):
    return quiver(0,0,y,x, scale_units='xy', angles='xy', scale=1)

fig = figure(figsize=(10,10))


plot(x,y, color='g', linestyle='--')
vetor(1,2)
T(1,2)
xlim(-5,5)
ylim(-5,5)
grid()
show()