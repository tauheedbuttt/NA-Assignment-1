from Polynomial import *
from Gauss import *

x1 = Polynomial({'x2': 1/4, 'x4': 1/4}, 0)
x2 = Polynomial({'x1': 1/4, 'x3': 1/4, 'x5': 1/4}, (5/4))
x3 = Polynomial({'x2': 1/4, 'x6': 1/4}, 0)
x4 = Polynomial({'x1': 1/4, 'x5': 1/4}, (3/2))
x5 = Polynomial({'x2': 1/4, 'x4': 1/4, 'x6': 1/4}, (-1/2))
x6 = Polynomial({'x3': 1/4, 'x5': 1/4}, (3/2))

k = 10

# print(x2.evaluate({'x1': 0, 'x3': 0, 'x5': -0.5}))

print('-----------------------------------Equations-----------------------------------')
print(f"x1 = {x1}")
print(f"x2 = {x2}")
print(f"x3 = {x3}")
print(f"x4 = {x4}")
print(f"x5 = {x5}")
print(f"x6 = {x6}")
print()

print('-----------------------------------JACOBI-----------------------------------')
iteration = jacobi([x1, x2, x3, x4, x5, x6], k)
print_iterations(iteration)

print()
print('-----------------------------------SEIDEL-----------------------------------')
iteration = siedel([x1, x2, x3, x4, x5, x6], k)
print_iterations(iteration)
