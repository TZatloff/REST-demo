items = ['pen', 'book', 'carD', 'phone']
for item in items:
    if item.lower().endswith('d'):
        items.remove(item)

print(items)

is_phone =  'phone' in items
if is_phone:
    print("111")

# numbers = [1, 2, 3, 4]
#
# my_dict = {k: v for k, v in zip(items, numbers)}
# print(my_dict)
#
# for k, v in my_dict.copy().items():
#     if not v % 2 == 0:
#         my_dict.pop(k)
#
# print(my_dict)
#
# items[1] = 'table'
# print(items[::-1])
#
# for n in numbers:
#     if n % 2 == 0:
#         print(n, end=" ")
#
# room = ('window', 'door', 'chair')
#
# room = list(room)
# room[1] = 'lamp'
# room = tuple(room)
# print(room)
#
# import random
#
# start_num = int(input("Enter start number: "))
# end_num = int(input("Enter end num: "))
#
# random_num = random.randint(start_num, end_num)
# num = 0
# print(random_num)
# while num <= end_num:
#     for elem in range(start_num, end_num):
#         if elem == random_num:
#             continue
#         else:
#             print(elem)
#             num += 1

float_number = 2.3453224
print(round(float_number))
print(f"{float_number:.2f}")

