import math
def slieve(n):
    number_list = [k for k in range(n+1)][2:] 
    for i in range(math.floor(n**0.5)):
        multiplier = 1
        r = number_list[i]*multiplier 
        while r <= n:
            if r == number_list[i]:
                pass    
            else:
                try: 
                    number_list.remove(r)
                except ValueError:
                    pass
                    
            multiplier += 1 
            r = number_list[i]*multiplier
    return number_list 