# from operator import index
#
# nums = [1, 2, 3, 4, 5]
#
# print(nums[2])
#
# #
# # print(nums[2:-1])
# #
# # print(nums[::2])
# #
#
# print(nums[2])  # 3
# print(nums[:2])  # 1, 2
# print(nums[::2])  # 1, 3, 5
# print(nums[::-2])  # 5, 3, 1
# print(nums[:-2])  # 1, 2, 3
# print(nums[-2])  # 4
#
# data = nums[::2]
# print(data)
#
# data1 = data[::-1]
# print(data1)
#
# test = "Michel Jordan"
#
# name = test[:6]
# print(name)
#
# lastname = test[-6:]
# print(lastname)
#
# phone = "1-123-456-7890"
# url = "https://example.com/page"
# code = "ABCD-1234-EFGH-23DW"
#
# test = "Hello|Test"
#
# print(phone[8:])
# a = phone.split("-")
# print(phone.split("-")[-1])
# print(url[8:19])
#
# print(url.split("/")[-2])
#
# print(code.split("-")[-3])


# result = "banana" in fruits
# print(result)
#
# if "grape" not in fruits:
#     print("You forget buy grape ")

# fruits = ["apple", "banana", "cherry"]
# grape = "grape" in fruits
#
# print(grape)
#
# if not grape:
#     print("You forget buy grape")
#
# name = "Jonathan"
#
#
# o = "o" in name
# print(o)
#
# if o:
#     print(name.replace("o", "a"))
#
#
# prices = {
#     "coffee": 3.5,
#     "tea": 2.0
# }
# coffee_p = prices.get("coffee")
# coffee_price = prices['coffee']
# print(coffee_price)
# print(coffee_p)
#
# if "coffee" in prices:
#    if prices.get("coffee") == 3.0:
#        print("Buy coffee")
#    else:
#        print(prices.get("coffee"))
#
# if "coffee" in prices and prices.get("coffee") == 3.1 or "tea" in prices and prices.get('tea') == 2.1:
#     print("Buy coffee or tea")
# else:
#     print(prices.get("coffee"))
#
#
#
# tea = 'tea' in prices
# coffee = 'coffee' in prices
#
# if tea or coffee:
#     print("both are available")
# else:
#     print('there are not tea or/and coffee')



class CustomMoney():
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return self.amount + other.amount


    def __eq__(self, other):
        return self.amount == other.amount

    def __sub__(self, other):
        return self.amount - other.amount



my_money = CustomMoney(250)
your_money = CustomMoney(100)

result_sub = my_money - your_money
result_add = my_money + your_money
result_eq = my_money == your_money
print(result_eq)
print(result_sub)
print(result_add)
