##Cryptographic Algorithm 01

# This'll be a quick test of an idea I've been playing with for quite some time
# now.

import random, math

def creorder(plaintext, key): #cipher reorder
     # Make the key and plaintext an array of integers
     try:
         plaintext = bytes(ciphertext, "UTF-8")
     except TypeError:
         print("Plain text already bytes...\nNice one! :)")
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
        print("Plain text already bytes...\nNice one! :)")
    key = bytes(key, "UTF-8")
    ciphertext = []

    for index, char in enumerate(plaintext):
        #print(index, char, char+key[index%len(key)])
        ciphertext.append(char+key[index%len(key)])

    return bytes(ciphertext)

def dreorder(ciphertext, key): #decipher reorder
    # make the key and the ciphertext an array of integers
    try:
        ciphertext = bytes(ciphertext, "UTF-8")
    except TypeError:
        print("ciphertext already bytes...\nNice one! :)")

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
        print("ciphertext already bytes...\nNice one! :)")
    key = bytes(key, "UTF-8")
    plaintext = []
    for index, char in enumerate(ciphertext):
        plaintext.append(char-key[index%len(key)])
    return "".join([chr(i) for i in plaintext])


def gen_random_key(length):
    output = ''
    for i in range(length):
        output += chr(random.randrange(ord("A"), ord("z")))

    return output
key = gen_random_key(5)
print("key:", key)
#print("output:",decipher(cipher(gen_random_key(4000), key), key))

def test_shift_integrity():
    right, wrong = 0, 0
    print("Testing the shifting integrity...")
    for j in range(100):
        i = gen_random_key(5000)
        key = gen_random_key(15)
        o = dshift(cshift(i, key), key)
        if i == o:
            right+=1
        else:
            wrong+=1
    print("Percentage correct: {0}%\nPercentage incorrect: {1}%".format(right, wrong))

def test_reorder_integrity():
    right, wrong = 0, 0
    print("Testing the reorder integrity...")
    for j in range(100):
         i = gen_random_key(5000)
         key = gen_random_key(15)
         o = dreorder(creorder(i, key), key)
         if i == o:
             right+=1
         else:
            wrong+= 1
         print("{0}% complete".format(j+1))

    print("Percentage correct: {0}%\nPercentage incorrect: {1}%".format(right, wrong))

test_reorder_integrity()
test_shift_integrity()
