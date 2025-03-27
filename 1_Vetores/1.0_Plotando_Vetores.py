# Plotando Vetores em R²

from pylab import*

#Criei uma função para plotar vetores em python
#quiver(0,0,x,y, scale_units='xy', angles='xy', scale=1)

def vetor(x,y):
    return quiver(0,0,x,y, scale_units = 'xy', angles='xy', scale=1)

vetor(1,1)
vetor(-1,-1)
vetor(1,-1)
vetor(-1,1)
xlim(-3,3)
ylim(-3,3)
grid()
show()