#!/bin/python3

# somehow encrypt things by putting them into one or many 3d shapes and performing
# a series of 3d transformations to that/those shapes.

# this is going to need:
# (See README.md)

import random, time, sys, math

def gen_random_key(length):
    output = ''
    for i in range(length):
        output += chr(random.randrange(ord("A"), ord("z")))

    return output

def generate_series_of_cubes(total):

    cubes = []
    dimentions = []
    sum_of_cubes = total
    #the `sum_of_cubes must` equal `total` when the function returns

    #find the maximum possible value for the cube that would fit.
    maximum_cube = int(total ** (1 / 3.0))

    while total != sum(cubes):
        #if not maximum_cube == 1:
        #    cube_size = random.randrange(1, maximum_cube)
        #else:
        #    cube_size = 1
        cube_size = maximum_cube
        sum_of_cubes -= cube_size**3

        cubes.append(cube_size**3)
        dimentions.append(cube_size)

        maximum_cube = int(sum_of_cubes ** (1 / 3.0))
        print("max:", maximum_cube,"this size:", cube_size, "total sum:",sum_of_cubes)

    print(sum(cubes))

    #reorder those cubes
    #you can't use random.shuffle - the cubes have to be reordered.
    # ~random.shuffle(cubes)~


    #return
    if sum(cubes) == total:
        return dimentions
    else:
        #something's wrong here, so throw an error!
        return None

def r_swap(l, pos1, pos2): #swap by reference
    x = len(l)
    temp_i = l[pos1 % x]
    l[pos1 % x] = l[pos2 % x]
    l[pos2 % x] = l[pos1 % x]

def ereorder_cubes(cubes, key):
    # cubes = passed by ref
    # key passed by value
    key = bytes(key, "UTF-8")

    iterations = key[0] * key[1]


    for number in range(iterations):
        r_swap(cubes, key[number % len(key)], key[(number+1) % len(key)])

def dreorder_cubes(cubes, key):
    # cubes = passed by ref
    # key = passed by value
    key = bytes(key, "UTF-8")

    iterations = key[0] * key[1]

    for number in range(iterations):
        r_swap(cubes, key[number % len(key)], key[(number+1) % len(key)])


key = gen_random_key(15)
cubes = generate_series_of_cubes(random.randrange(0, 142672987))
print(cubes)
ereorder_cubes(cubes, key)
print(cubes)
dreorder_cubes(cubes, key)
