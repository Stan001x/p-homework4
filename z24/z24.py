import random
size = int(input("Введите количество кустов на грядке: "))
my_list = list(random.randint(1, 10) for _ in range(size))
print(my_list)
maximum = my_list[size-2] + my_list[size-1] + my_list[0]
if my_list[size-1] + my_list[0] + my_list[1] > my_list[size-2] + my_list[size-1] + my_list[0]:
    maximum = my_list[size-1] + my_list[0] + my_list[1]
for i in range(1, size - 2):
    if my_list[i-1] + my_list[i] + my_list[i+1] > maximum:
        maximum = my_list[i-1] + my_list[i] + my_list[i+1]

print(maximum)
