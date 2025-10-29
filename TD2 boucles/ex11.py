def u_iter(n):
    if n < 0:
        return -1
    u = 1.0  
    i = 0
    while i < n:
        u = u / (u + 1)
        i += 1
    return u

print(u_iter(5))    
