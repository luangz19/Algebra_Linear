# Algumas transformações Lineares

from pylab import*

# Exemplo: T:R²->R², onde T(x,y) = (-y,x)

def T(x,y):
    return quiver(0,0,-y,x, scale_units='xy', angles='xy', scale=1)

def vetor(x,y):
    return quiver(0,0,x,y, scale_units='xy', angles='xy', color='b', scale=1)

fig = figure(figsize=(10,10))

vetor(-1,2) # vetor 
T(-1,2)  # T transforma o vetor (-1,2) em T(-1,2) = (-2,-1) 

xlim(-5,5)
ylim(-5,5)
grid()
show()