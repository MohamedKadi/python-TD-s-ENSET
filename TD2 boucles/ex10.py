def approx(epsi):
    if epsi > 0:
        n = 0
        fact = 1        
        u = 1.0         
        while 3 / fact > epsi:
            n += 1
            fact *= n           
            u += 1 / fact       
        return u    
    else:
        print("il faut que epsi est strictement positive")