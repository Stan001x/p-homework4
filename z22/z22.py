import random
size1 = int(input("Ведите количество элементов первого множества: "))
size2 = int(input("Ведите количество элементов второго множества: "))

my_list1 = set(random.randint(1, 10) for _ in range(size1))
my_list2 = set(random.randint(1, 10) for _ in range(size2))
finish_list = set.intersection(my_list1, my_list2)
print(list(finish_list))
