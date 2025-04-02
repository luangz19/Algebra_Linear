import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

def axvetor(x,y,z):
    o = [0,0,0]
    v = [x,y,z]
    ax.quiver(*o,*v, color='b', arrow_length_ratio=0.1)

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

