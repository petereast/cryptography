# Shift'n'shuffle testing suite

from shufflenshift import *

def test_cipher_integrity():
    right, wrong = 0, 0
    print("Testing combined integrity of the cipher...\nChunksize: 5 KiloBytes")
    for j in range(0, 100):
        i = gen_random_key(1024*5)
        key = gen_random_key(15)
        o = decipher(cipher(i, key), key)
        if i == o:
            right += 1
        else:
            wrong +=1
    return right

def test_shift_integrity():
    right, wrong = 0, 0
    print("Testing the shifting integrity...")
    for j in range(100):
        i = gen_random_key(1024*5)
        key = gen_random_key(15)
        o = dshift(cshift(i, key), key)
        if i == o:
            right+=1
        else:
            wrong+=1
    return right

def test_reorder_integrity():
    right, wrong = 0, 0
    print("Testing the reorder integrity...")
    for j in range(100):
         i = gen_random_key(1024*5)
         key = gen_random_key(15)
         o = dreorder(creorder(i, key), key)
         if i == o:
             right+=1
         else:
            wrong+= 1
    return right


x = test_reorder_integrity()
x += test_shift_integrity()
x += test_cipher_integrity()

print("All good :)" if x == 300 else "There's an error somewhere")
