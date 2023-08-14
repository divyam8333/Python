lst = [1, 2, 3, 1, 5, 42,1]

list_size = len(lst)

print("Idicies of all Occurence of a given element in a given list is:")
for itr in range(list_size):
	if(lst[itr] == 1):
		print(itr)
