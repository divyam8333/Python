lst = [1, 2, 3, 1, 5, 42,1]
n=int(input("Enter an element you want to search in list:"))

list_size = len(lst)

print("Index no. of",n,"in a given lsit is:")
for itr in range(list_size):
	if(lst[itr] == n):
		print(itr)
