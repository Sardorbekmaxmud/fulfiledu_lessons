# name = input("Ismingizni kiriting:\n")
# interes = input("Qiziqishlaringizni kiriting:\n")

# # if any([x in interes for x in ['kitob','kutubxona']]):
# if 'kitob' in interes or "kutubxona" in interes:
#     book_lib = input('qanday kitoblar yoqadi?\n')
#     if "detektiv" in book_lib:
#         book = input("shaytanat kitobi haqidagi fikringiz?\n")
#         print("Raxmat, fikrlaringiz uchun!")
#     elif "diniy" in book_lib:
#         print("Sizga 'Hadis va hayot' kitoblar to'plamini sovg'a qilamiz!")
#     else:
#         print("Ajoyib narsalarga qiziqar ekansiz!")
# elif 'sport' in interes:
#     savol = input("qaysi sport turiga qiziqasiz?\n")
#     if 'futbol' in savol:
#         f_club = input("qaysi komandani yoqtirasiz?\n")
#         if "real" in f_club or 'barsa' in f_club:
#             print("el-classicoga chipta sovg'a qilamiz!🎉")
#         else:
#             print("Ajoyib, komandangizga zafarlar tilaymiz")
#     else:
#         print("Sport bilan shug'ullanish sog'lik garovi")
# else:
#     print("Ko'p narsalarga qiziqar ekansiz, bu ajoyib!")



#---------------------------------------------------------------------------------------

# # 1
# k = int(input("k: "))
# n = int(input("n: "))

# for i in range(n):
#     print(k)

# # 2
# n = int(input("n: "))
# answer = 0
# for i in range(1,n+1,2):
#     answer+=i
# print(answer)

# # 3
# n = int(input("n: "))
# answer = 0
# for i in range(n+1):
#     if i%3==0 and i%9!=0:
#         answer+=i
# print(answer)

# # 4
# n = int(input("n: "))
# answer = 0
# for i in range(1,n+1):
#     answer+=i**2
# print(answer)

# # 5
# word = input("soz kiriting: ")
# word_len = int(input(f"1-{len(word)} oralig'ida son kiriting: "))

# answer=''
# for i in word:
#     if word.index(i)==word_len-1:
#         continue
#     answer+=i
# print(answer)

# # 6
# price = int(input("narxni kiriting: "))
# if price>100_000:
#     print(f"sizga {(price*90)//100} so'm")
# elif price > 50_000:
#     print(f"sizga {(price*95)//100} so'm")
# else:
#     print(f"{price} so'm")

# # 7
# natija=[]
# a = int(input("a: "))
# b = int(input("b: "))
# for i in range(b-1,a,-1):
#     natija.append(i)
#     print(i)
# print("Uzunligi: ",len(natija))


# # 8
# sweet_price = int(input("kanfet narxi: "))
# for kg in range(1,11):
#     print("{} kg narxi: {:,} so'm".format(kg,kg*sweet_price))

# # 9
# sweet_price = int(input("kanfet narxi: "))
# for kg in range(1,11):
#     print("{} kg narxi: {:,} so'm".format(kg/10,kg/10*sweet_price))

# # 10
# natija=0
# a = int(input("a: "))
# b = int(input("b: "))
# for i in range(a,b+1):
#     natija+=i**2
#     print(f"{i} kvadrati = {i**2}")
# print("yig'indi: ",natija)

# # 11
# a = int(input("a: "))
# n = int(input("n: "))
# for i in range(1,n+1):
#     print(f"{a} ning {i} darajasi = ",a**i)

# # 12 factorial
# son = int(input("son kiriting: "))
# natija = 1
# for i in range(1,son+1):
#     natija*=i
# print(natija)