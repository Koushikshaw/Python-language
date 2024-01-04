""""
STAIRS PROBLEM
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


import math
print("Counting number of ways we can walk to stairs")
a = int(input("Enter the number of stairs : "))
i=0
result = 0
while (a-i)>=i:
    result = result + (math.factorial(a-i)/(math.factorial(i)*math.factorial(a-2*i)))
    i=i+1

print("The number of ways are : ",result)
    
    
    
