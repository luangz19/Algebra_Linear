# Seja x = (x1 , x2 , . . . , xn ). A norma de x é dada por
# ||x|| = (<x,x>)½ = ((x1)² + ··· + (xn)²)½ é norma euclidiana

from pylab import*
from plot_vetores import*
from numpy import*

# Vetores em R²

x = array([1,2])

#print(f'Norma  ||{x}|| = {linalg.norm(x)}')

def norma(x,y):
    return (x**2 + y**2)**(1/2)

#print(f'\nNomra de ||x|| = ||(1,2)|| = {norma(1,2)}')

fig = figure(figsize=(10,10))

vetor(1,2)
coord(1,2)
xlim(-5,5)
ylim(-5,5)
grid()
show()