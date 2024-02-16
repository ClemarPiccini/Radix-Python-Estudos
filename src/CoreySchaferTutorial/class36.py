###Os generators são úteis quando você precisa lidar com grandes quantidades de dados ou quando deseja criar sequências de valores de forma eficiente, evitando o armazenamento desnecessário na memória.
def square_numbers(nums):
    for i in nums:
        yield(i*i)

my_nums = square_numbers([1, 2, 3, 4, 5])

print (next(my_nums))
print (next(my_nums))
print (next(my_nums))
print (next(my_nums))
print (next(my_nums))

##Exemplo de generators com list compression
#my_nums = [x*x for x in [1, 2, 3, 4, 5]]

for num in my_nums:
    print (num)