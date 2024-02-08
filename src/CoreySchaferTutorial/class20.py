nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#I want 'n' for each 'n' in nums 
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

#compressao de lista 
my_list = [n for n in nums]
print(my_list)

#I want 'n*n' for each 'n' in nums 
my_list = []
for n in nums:
    my_list.append(n*n)
print(my_list)

#compressao de lista
my_list = [n*n for n in nums]
print(my_list)

#Using a map + lambda
my_list = map(lambda n: n*n, nums)
print (my_list)

