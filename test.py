def birthday(s, d, m):
    # Write your code here
    sum = 0
    count = 0
    for i in range(0,len(s)-m+1):
        sum = 0
        for j in range(i,i+m):
            sum = sum + s[j]
        print(f"s {sum} + {d}")
        if sum == d:
            count += 1
    return count

print(birthday([4],4,1))