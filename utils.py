import math
def filter_f(s): 
    if int(str(s)[-1]) in [1,3,7,9]:
        return True  
def slieve(n):
    if n <= 10: 
        number_list = [k for k in range(n+1)][2:]
    else:
        
        number_list = [2,3,5,7] + [k for k in range(10,n+1,1) if filter_f(k) == True]
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
