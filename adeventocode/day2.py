


"""
Docstring for adeventocode.day2
"""

sol = """4487-9581,755745207-755766099,954895848-955063124,4358832-4497315,15-47,1-12,9198808-9258771,657981-762275,6256098346-6256303872,142-282,13092529-13179528,96201296-96341879,19767340-19916378,2809036-2830862,335850-499986,172437-315144,764434-793133,910543-1082670,2142179-2279203,6649545-6713098,6464587849-6464677024,858399-904491,1328-4021,72798-159206,89777719-90005812,91891792-91938279,314-963,48-130,527903-594370,24240-60212"""

def validProducts(nums_arr):
    sum = 0
    for i in nums_arr:
        #print(i)
        num = i.split("-")

        first_num = num[0]
        second_num = num[1]

        len_second_num = len(second_num)

        mid = len_second_num // 2
        
        for j in range(int(first_num), int(second_num) + 1):
            if(len(str(j)) >= mid):
                if(str(j)[:mid] == str(j)[mid:]):
                    #print("j : " + str(j))
                    sum += j
    return sum

        



        
nums_arr = sol.strip().split(",")

print(validProducts(nums_arr))