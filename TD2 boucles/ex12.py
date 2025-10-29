def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    u_prev, u_curr = 1, 1
    for i in range(2, n + 1):
        u_prev, u_curr = u_curr, u_curr + u_prev
    return u_curr

def v_n(n):
    u_n_plus_1 = fibonacci(n + 1)
    u_n_minus_1 = fibonacci(n - 1)
    u_n = fibonacci(n)
    return u_n_plus_1 * u_n_minus_1 - u_n * u_n

#print("fibonacci sequence:")
#for i in range(15):
#    print(f"u_{i} = {fibonacci(i)}")

#print("\valeurs de v_n:")
#for n in range(1, 16):
#    print(f"v_{n} = {v_n(n)}")
