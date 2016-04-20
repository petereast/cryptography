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


def creorder(plaintext, key): #cipher reorder
     # Make the key and plaintext an array of integers
     try:
         plaintext = bytes(plaintext, "UTF-8")
     except TypeError:
        #print("Plain text already bytes...\nNice one! :)")
        pass
     key = bytes(key, "UTF-8")
     # Take the plaintext in blocks of four (or more) characters
     blocksize = 4
     output = []
     for index in range(0, len(plaintext), blocksize):
         keychar = key[index%len(key)]
         block = plaintext[index:index+blocksize]
         blocksize = len(block)
         # reorder the block according to the key

         reordered_block = [None]*blocksize

         for index, char in enumerate(block):
             ##print(chr(keychar), (keychar+index)%blocksize)
             reordered_block[index] = block[(keychar+index)%blocksize]

         reordered_block = "".join([chr(o) for o in reordered_block])
         #print(keychar, block, reordered_block)

         output += reordered_block

     #Begin the second stage of the cipher
     #print("output: ", "".join(output))
     return "".join(output)

def dreorder(ciphertext, key): #decipher reorder
    # make the key and the ciphertext an array of integers
    try:
        ciphertext = bytes(ciphertext, "UTF-8")
    except TypeError:
        #print("ciphertext already bytes...\nNice one! :)")
        pass
    key = bytes(key, "UTF-8")

    #take the cipher in blocks
    blocksize = 4
    output = []
    for index in range(0, len(ciphertext), blocksize):
        keychar = key[index%len(key)]
        block = ciphertext[index:index+blocksize]
        blocksize = len(block)

        ordered_block = [None]*blocksize

        for index, char in enumerate(block):
            ordered_block[index] = block[(index - keychar)%blocksize]
        ordered_block = "".join([chr(o) for o in ordered_block])
        output+= ordered_block
        #print(keychar, block, ordered_block)
    return "".join(output)

def r_swap(src, pos_a, pos_b):
    tmp = src[pos_a]
    src[pos_a] = src[pos_b]
    src[pos_b] = tmp

def dreorder_cubes(cubes, key):
    # cubes = passed by ref
    # key = passed by value
    key = bytes(key, "UTF-8")

    iterations = key[0] * key[1]

    for number in range(iterations):
        r_swap(cubes, key[number % len(key)] % len(cubes), key[(number+1) % len(key)] % len(cubes))

def ereorder_cubes(cubes, key):
    # Cubes by ref
    # Key by value

    key = bytes(key, "UTF-8")
    iterations = key[0] * key[1]

    for number in range(iterations):
        r_swap(cubes, key[number % len(key)] % len(cubes), key[(number+1) % len(key)] % len(cubes))


key = gen_random_key(15)
cubes = generate_series_of_cubes(random.randrange(0, 142672987))
print(cubes)
ereorder_cubes(cubes, key)
print(cubes)
dreorder_cubes(cubes, key)
