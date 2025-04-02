# Sejam x = (x1 , x2 , . . . , xn ) e y = (y1 , y2 , . . . , yn ). O produto escalar (ou interno) de x por y , indicado por <x,y> , é o número real dado por
# <x,y> = x1·y1 + x2·y2 + · · · + xn.yn. 
# onde <·,·>:R^n -> R

from numpy import*

x = array([1,2])
y = array([2,3])

z = array([2,3,4,5,7])
w = array([5,-6,7,9,8])

print(x@y) # produto interno

print(f'\n{z@w}')