#!/bin/python3

# somehow encrypt things by putting them into one or many 3d shapes and performing
# a series of 3d transformations to that/those shapes.

# this is going to need:
# (See README.md)

import random, time, sys, math

def generate_series_of_cubes(total):

    cubes = []
    sum_of_cubes = total
    #the `sum_of_cubes must` equal `total` when the function returns

    #find the maximum possible value for the cube that would fit.
    maximum_cube = round(total ** (1 / 3.0))

    while total != sum(cubes):
        #if not maximum_cube == 1:
        #    cube_size = random.randrange(1, maximum_cube)
        #else:
        #    cube_size = 1
        cube_size = maximum_cube
        sum_of_cubes -= cube_size**3

        cubes.append(cube_size**3)

        maximum_cube = int(sum_of_cubes ** (1 / 3.0))
        print("max:", maximum_cube,"this size:", cube_size, "total sum:",sum_of_cubes)

    print(sum(cubes))

    #reorder those cubes
    #you can't use random.shuffle - the cubes have to be reordered.
    # ~random.shuffle(cubes)~

    


    #return
    if sum(cubes) == total:
        return cubes
    else:
        #something's wrong here, so throw an error!
        return None

print(generate_series_of_cubes(140))
