
from functools import reduce

# nb_G = 5400.4
# print(f"hello {nb_G:.0e}")

# def test(**args):
#     print(args)
#     print(args.items()) #array of tuple
#     for c,v in args.items():
#         print(c , v)

# test(nom="mohamed",age=12, vamos="heee")

##############################""" lambda"
# x = lambda a : a + 10
# print(x(5)) #10+5

# x = lambda a,b : a+b
# print(x(5, 6)) #5*6

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))

# #input
# print("Enter your name:")
# name = input() 
# print(f"Hello {name}")


##############################""" map"
# def carre(x):
#     return x**2

# some = [1,2,3,4,5]
# list1 = [1,2,3,4,5]

# new_list = map(carre,some)
# print(new_list)
# print(list(new_list))


##############################""" filter"
# persons = [1,2,3,4,5,6,7,8,9,10]
# new_pers = filter(lambda a : a >= 5, persons)
# print(list(new_pers))


##############################""" reduce"
# def add(x,y):
#     return x+y

# nums = [9,2,3,4,5]

# result = reduce(lambda a,b : add(a,b) ,nums)
# max = reduce(lambda a,b : a if a > b else b,nums)
# print((max))

##############################""" zip"
# con = [1,2,3,4,5,8,10]
# dest = [5,4,3,2,1,7]

# resu = zip(con,dest)

# print(list(resu))


##############################""" mutable"
#mutable list sets dicts
#inmutable nums string tuple


##############################""" list"
# lis = [1,2,3,4,5]

# lis.append(6)
# lis.insert(2,"heelo")
# print(lis)
# #lis.pop(1)
# lis.remove(1)
# print(lis)

##############################""" tuples"
# tuple_ex = ([1,2,3],4)
# tuple_ex[0].append(5)
# print(tuple_ex)


##############################""" sets" seance 4

set_ex = {1,2,3,4,5,5}
settt = set(set_ex) #remove doublement
settt2 = {5,6,7,8}
# settt.add(7)
# settt.add(4)
# settt.remove(4)
print(settt & settt2)
print(settt | settt2)
print(settt ^ settt2)
print(settt - settt2)


##############################""" dicts" seance 4
# test = {
#     "nom": "mohamed",
#     "age":20
# }
# #test.pop("age")
# test["nom"] = "hii"
# #print(test.get("age"))
# for x,y in test.items(): #keys or values
#     print(x, y)


########################################################q 1
# temperatures = [-15, -5, 0, 20, 25, 30]
# # Expected: [(-5, 23.0), (0, 32.0), (20, 68.0), (25, 77.0), (30, 86.0)] (F = C × 9/5 + 32)

# def changeC(temp):
#     if(temp > -10):
#         F = temp * 9/5 + 32
#         return (temp,F)
#     return 

# new_temp = map(changeC,temperatures)
# new_2 = [item for item in new_temp if item is not None]
# print(new_2)
########################################################q 2
# data = ["123", "hello", "45.6", "world", "789", "3.14", "test"]
# # Expected: [123, 'hello', 45.6, 'world', 789, 3.14, 'test']
# def convert(item):
#     try:
#         return int(item)
#     except ValueError:
#         try:
#             return float(item)
#         except ValueError:
#             return item
    
# new_list = [convert(item) for item in data]
# print(new_list)

########################################################q 3
# words = ["apple", "banana", "cherry", "date", "elderberry"]
# # Expected: "elderberry" (or ("elderberry", 4) if including index)

# def maxlen(a, b):
#     if len(a) > len(b):
#         return a[1],a[0]
#     return b[1],b[0]

# new_word = reduce(maxlen ,enumerate(words))

# print(new_word)
########################################################q 4
# numbers = [4, 2, 8, 6, 5]
# # Expected: (25, 5, 5.0)  # (sum, count, average)
# total, count = reduce(lambda acc, y: (acc[0]+y, acc[1]+1),numbers,(0,0))

# print((total, count, total/count))
########################################################q 5
# nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]
# # Flattened: [1,2,3,4,5,6,7,8,9,10], Even sum: 2+4+6+8+10 = 30
# # Expected: 30
# sum_even = reduce(lambda acc, nested: acc + sum(n for n in nested if n%2==0), nested,0)
# print((sum_even))

########################################################q 6
# keys = ["name", "age", "_id", "score", "None", "address"]
# values = ["John", 25, None, 85, "test", "NYC"]
# # Expected: {"name": "John", "age": 25, "score": 85, "address": "NYC"}
# lii = zip(keys,values)
# print(dict(lii))

########################################################
def manage_grades(grades):
    step1 = list(filter(lambda a : a > 40 , grades))
    step2 = list(map(lambda a: a+5,step1))
    (step2.sort(reverse=True))
    step4 = (step2[0] + step2[1]+ step2[2]) / 3
    return round(step4)

# Test case
grades = [35, 67, 89, 42, 55, 38, 91, 76, 33, 95]
result = manage_grades(grades)
print(f"Average of top 3: {result}")
# Expected output: Average of top 3: 98.0
# Explanation: 
# Step 1: Remove <40 → [67, 89, 42, 55, 91, 76, 95]
# Step 2: Add 5 → [72, 94, 47, 60, 96, 81, 100]
# Step 3: Sort desc → [100, 96, 94, 81, 72, 60, 47]
# Step 4: Average of top 3 → (100+96+94)/3 = 96.67


