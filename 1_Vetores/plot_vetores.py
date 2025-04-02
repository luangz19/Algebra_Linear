from pylab import*

def vetor(x,y):
    return quiver(0,0,x,y, scale_units = 'xy', angles='xy', color='b', scale=1)

def coord(x,y):
    plot([x,x],[0,y], color='g', linestyle='--')
    plot([0,x],[y,y], color='g', linestyle='--')
