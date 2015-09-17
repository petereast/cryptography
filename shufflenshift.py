##Cryptographic Algorithm 01

# This'll be a quick test of an idea I've been playing with for quite some time
# now.

import random, math, time

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

def cshift(plaintext, key): #cipher shift
    # This is a twist on a tradition Caesar Shift, each character is changed by
    # the value of the key.
    try:
        plaintext = bytes(plaintext, "UTF-8")
    except TypeError:
       #print("Plain text already bytes...\nNice one! :)")
       pass
    key = bytes(key, "UTF-8")
    ciphertext = []

    for index, char in enumerate(plaintext):
        #print(index, char, char+key[index%len(key)])
        ciphertext.append(char+key[index%len(key)])

    return bytes(ciphertext)

def cipher(plaintext, key):
    # Generate a cipher using a combination of the two sub-ciphers
    # Reorder the plaintext first...
    plaintext = creorder(plaintext, key)
   #print(plaintext)

    # Shift the plaintext
    ciphertext = cshift(plaintext, key)
    return ciphertext

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

def dshift(ciphertext, key):
    try:
        ciphertext = bytes(ciphertext, "UTF-8")
    except TypeError:
        #print("ciphertext already bytes...\nNice one! :)")
        pass
    key = bytes(key, "UTF-8")
    plaintext = []
    for index, char in enumerate(ciphertext):
        plaintext.append(char-key[index%len(key)])
    return "".join([chr(i) for i in plaintext])

def decipher(ciphertext, key):
    # This should undo the damage done by the first cipher process
    # Get the cipher back into it's original order
   #print("C:",ciphertext)
    ciphertext = dshift(ciphertext, key)
    # De shift the ciphertext...
    plaintext = dreorder(ciphertext, key)
    return plaintext

def gen_random_key(length):
    output = ''
    for i in range(length):
        output += chr(random.randrange(ord("A"), ord("z")))

    return output
key = gen_random_key(5)#print("key:", key)
#print("output:",decipher(cipher(gen_random_key(4000), key), key))
#print(cipher("hello world", key))#print(decipher(cipher("hello world", key), key))
