# Seja x = (x1 , x2 , . . . , xn ). A norma de x é dada por
# ||x|| = (<x,x>)½ = ((x1)² + ··· + (xn)²)½ é norma euclidiana

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

# Vetores em R³

def norma(x,y,z):
    return (x**2 + y**2 + z**2)**(1/2)

#print(f'\nNorma de ||x|| = ||(3,4,-5)|| = {norma(3,4,-5)}')

def axvetor(x,y,z):
    o = [0,0,0]
    v = [x,y,z]
    ax.quiver(*o,*v, color='b', arrow_length_ratio=0.1)


fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
axvetor(2,2,0)
axvetor(0,2,2)
axvetor(2,0,2)
axvetor(2,2,2)
ax.scatter(2,2,0, color='r')
ax.scatter(0,2,2, color='g')
ax.scatter(2,0,2, color='yellow')
ax.scatter(2,2,2, color='orange')
ax.set_xlim([0,4])
ax.set_ylim([0,4])
ax.set_zlim([0,4])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()