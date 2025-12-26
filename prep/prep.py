
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

# set_ex = [1,2,3,4,5,5]
# settt = set(set_ex) #remove doublement
# settt2 = {5,6,7,8}
# settt.add(7)
# settt.add(4)
# settt.remove(4)
# print(settt & settt2)
# print(settt | settt2)
# print(settt ^ settt2)
# print(settt - settt2)


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


