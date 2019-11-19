# taken from https://www.geeksforgeeks.org/python-program-to-print-all-prime-numbers-in-an-interval/
start = 11
end = 25
  
for val in range(start, end + 1): 
      
   # If num is divisible by any number   
   # between 2 and val, it is not prime  
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
           print(val) 
    
