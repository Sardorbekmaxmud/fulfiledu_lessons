# def sanoq():
#     for i in range(1,41):
#         if i%2==0 and i%3==0:
#             print(i)

# sanoq()
###-------------------------------------------------------------------------------------------------------------
# # 1
# def user_data(first_name, last_name, age):
#     print(f"Ism: {first_name}\
#             \nFamiliya: {last_name}\
#             \nYosh: {age}")

# f_name = input('Ism: ')
# l_name = input('Familya: ')
# age = input('Yosh: ')
# user_data(f_name,l_name,age)

# # 2
# def find_max(a,b,c):
#     if a>b and a>c:
#         print(a)
#     elif b>c:
#         print(b)
#     else:
#         print(c)

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# find_max(a,b,c)

# # 3
# def find_letter_count(word,letter):
#     print(word.count(letter))

# word = input("So'z kiriting: ")
# letter = input("Harf kiriting: ")

# find_letter_count(word,letter)

# # 4
# def list_num(mylist):
#     print(len(mylist))

# list_1 = [32,5,6,4,'ere','bdb',45,'3431']
# list_num(list_1)

# # 5
# def daraja(a,b):
#     return a**b

# print(daraja(2,3))

# # 6
# def daraja4(a,b,c,d):
#     print(a**b)
#     print(c**d)

# daraja4(2,3,3,2)

# # 7
# def digit_count_and_sum(word):
#     count_num = 0
#     yigindi = 0
#     for letter in word:
#         if letter.isdigit():
#             count_num+=1
#             yigindi+=int(letter)
#     print(f"Sonlar yig'indisi: {yigindi} ta\nSonlar {count_num} ta qatnashgan")

# word_input = input("So'z: ")
# digit_count_and_sum(word_input)

# # 8
# def add_right(a, b):
#     print(f"{a}{b}")

# add_right(344,3245)

# # 9
# def add_left(a, b):
#     print(f"{b}{a}")

# add_left(44,32)

# # 10
# def work_with_list(a):
#     min_num = min(a)
#     for i in range(len(a)):
#         a[i] = a[i] ** min_num
#     print(a)

# work_with_list([2, 3, 4, 5, 6, 7, 8, 9])

# # 11
# def big_sales(sales):
#     month = list(sales.keys())[0]
#     salary = list(sales.values())[0]
#     for key,values in sales.items():
#         if salary<values:
#             month=key
#             salary=values
#     return month

# def big_sales(sales):
#     return max(sales,key=sales.get)

# print(big_sales({
#     "yanvar": 12000,
#     "mart": 6000,
#     "aprel": 15000,
#     "sentabr": 9000,
#     "dekabr": 10000,
# }))

# # 12
# def min_max(numbers, max_num, min_num):
#     if max(numbers)==max_num:
#         print(max_num,"numbers ichidagi eng katta son")
#     else:
#         print(max_num,"numbers ichidagi eng katta son emas")
#     if min(numbers)==min_num:
#         print(min_num,"numbers ichidagi eng kichik son")
#     else:
#         print(min_num,"numbers ichidagi eng kichik son emas")

# min_max([3,5,12,63,41,39,86,4],85,4)

# # 13
# def expensiveProduct(products):
#     p_name = products[0]['name']
#     p_price = products[0]['price']
#     for p in products:
#         if p_price<p['price']:
#             p_name=p['name']
#             p_price=p['price']
#     return p_name

def expensiveProduct(products):
    return max(products)

mylist = [
  {
    "name": "Iphone X",
    "price": 600
  },
  {
    "name": "Iphone 12",
    "price": 1500
  },
  {
    "name": "Samsung Note 9",
    "price": 800
  },
  {
    "name": "Samsung S10",
    "price": 1100
  },
]
print(expensiveProduct(mylist))