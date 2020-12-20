import random 
import math

ar = []

for x in range(10):

    ar.append(random.randint(1, 100))

print(ar)

def jump_measure(length_of_array):

    return int(math.sqrt(length_of_array))

def jump_indices(length_of_array):

    jump_indices = []
    jump_measuree = jump_measure(length_of_array)
    item = jump_measure(length_of_array)    

    while item <= length_of_array:
        jump_indices.append(item)
        item += jump_measuree

    return jump_indices

l = jump_indices(len(ar))
print(l)
print(jump_indices(16))
print(jump_indices(100))
print(jump_indices(400))
ar.sort()
print(ar.sort())
print(ar)
