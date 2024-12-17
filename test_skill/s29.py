my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list.remove(3)
my_list.append(3)

my_list = [w for w in my_list if w % 2 == 1]

print('my_list = ', my_list)