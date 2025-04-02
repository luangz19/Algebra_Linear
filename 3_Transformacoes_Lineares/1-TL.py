# Algumas transformações Lineares

from pylab import*

# Exemplo: T:R²->R², onde T(x,y) = (-y,x)

def T(x,y):
    return quiver(0,0,-y,x, scale_units='xy', angles='xy', scale=1)

fig = figure(figsize=(10,10))

T(-1,2)  # = (-2,-1)
T(-1,-2) # = (2,-1)
T(1,2)
T(1,-2)
T(1,0) # = T(e1)
T(0,1) # = T(e2)
xlim(-5,5)
ylim(-5,5)
grid()
show()