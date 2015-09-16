##Cryptographic Algorithm 01

# This'll be a quick test of an idea I've been playing with for quite some time
# now.

import random, math

def cipher(plaintext, key):
     # Make the key and plaintext an array of integers
     plaintext = bytes(plaintext, "UTF-8")
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
             #print(chr(keychar), (keychar+index)%blocksize)
             reordered_block[index] = block[(keychar+index)%blocksize]

         reordered_block = "".join([chr(o) for o in reordered_block])
         print(keychar, block, reordered_block)

         output += reordered_block

     #Begin the second stage of the cipher
     print("output: ", "".join(output))
     return "".join(output)

def decipher(ciphertext, key):
    # make the key and the ciphertext an array of integers
    ciphertext = bytes(ciphertext, "UTF-8")
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
        print(keychar, block, ordered_block)
    return "".join(output)

def gen_random_key(length):
    output = ''
    for i in range(length):
        output += chr(random.randrange(ord("A"), ord("z")))

    return output
key = gen_random_key(5)
print("key:", key)
print("output:",decipher(cipher("The quick brown fox jumped over the lazy dog", key), key))

results = []

# for i in range(100):
#     i = "The quick brown fox jumped of the lazy-ass dog"
#     key = gen_random_key(15)
#     o = decipher(cipher(i, key), key)
#     results.append(i == o)
#
# print(results)
