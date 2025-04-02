# Algumas transformações Lineares

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Função para o vetor
def axvetor(x,y,z):
    o = [0,0,0]
    v = [x,y,z]
    ax.quiver(*o,*v, color='b',  arrow_length_ratio=0.1)

# Definindo a transformação linear
def T(x,y,z):
    o = [0,0,0]
    v = [x+y,y-x,z+y]
    ax.quiver(*o,*v, color='r',  arrow_length_ratio=0.1)

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

axvetor(1,2,1)
T(1,2,3)

ax.set_xlim([0,6])
ax.set_ylim([0,6])
ax.set_zlim([0,6])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()