from pylab import*

# Defindo T:R²-> R² onde T(x,y) = (x+y,x-y)
def T(x,y):
    return quiver(0,0,x+y,x-y, scale_units='xy', angles='xy', scale=1)

fig = figure(figsize=(10,10))

T(2,-1)
T(3,-2)
T(-3,2)
T(1,0)
T(0,1)
xlim(-8,8)
ylim(-8,8)
grid()
show()