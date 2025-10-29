#question 1


op = ['+','-','*','/']
def polonaise(input):
    stack = []
    x = input.split()
    for element in x:
        if(element not in op):
            stack.append(element)
        else:
            if(len(stack) < 2):
                print("error")
                return
            num2 = int(stack.pop())
            num1= int(stack.pop())
            stack.append(eval(num1 + element + num2))
            
    return stack.pop()

print(polonaise("3 28 7 / +"))