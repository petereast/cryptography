# Reorder a pylist according to a key so it appears to be random, but can
# be reconstructed in it's original order

testing_list = [x for x in range(0, 100)]
key = bytes("Hello", "UTF-8")

def reorder(input_list, key):
	print("Reordering list...")


# RECURSIVE BLOCKS!!!

def sepblocks(inlist, blocksize): # seperate a list into seperate blocks

	outlist = []
	if len(inlist) == 1:
		return inlist
	else:
		while len(inlist) != 0:
			outlist.append(inlist[:blocksize])
			del inlist[:blocksize]
	return sepblocks(outlist, blocksize)

def is_list(test):
	return type(test) == list

def strip_list(inlist):
	# TODO: fix the data loss caused by this function
	while is_list(inlist[0]):
		inlist = inlist[0]
	return inlist

#TODO: make this more efficient! right now it's O(N^N)

print(sepblocks(testing_list.copy(), 2))
print(testing_list)
