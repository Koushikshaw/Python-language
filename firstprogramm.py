# for single line comment
"""
Multiline comment
like this
"""

#modules in python
import math

# Script starts
print("Hello World")

# list in python []
nums = []
nums.append(96)
nums.append("hello")
print(nums)

# input and output in python
# the return type of input function is a string
a = input("Enter a name ")
print("Hello ",a)

# to get a integer as input we need to typecast it to integer
b = int(input("Enter a number : "))
print(b)

#if statement in python
if(b>12):
    print("The number you entered is greater than 12")
elif(b<0):
    print("The number you entered is less than 0")
else:
    print("This is a else statement")
    
#user-defined-functions in python (def keyword)

    #function with no arguments but return
    def greet():
        return "hello"
    
    #function with argument but no return
    def greet1(name):
        print("Hello ",name)
    
    #function with argument and return
    def greet2(name):
        greet = "Hello "+name
        return greet
    
    #function with no argument no return
    def greet4(name):
        greet = "Hello "+name
        print(greet)
        
#Loops (for)
for step in range(5):
    print(step)
    
"""
'And'
and keyword returns the first false value
and if not found it returns the last value

for example :
3 and 0 returns 0
but 
4 and 10 returns 10 
as there is no false value so it returns the last value

---

'or'
or keyword returns the first true value
if not found it returns the last value

for example :
3 and 0 will return 3
but
0 or 0 will return 0

---

'not' inverts the value

---

'in' checks if container contains a value

---

'is' check if both object takes same memory location or not

---

Note : Two empty strings are identical but two empty dictionaries are not identical

---
"""
# class attribites
class Dog:
	attr1 = "mammal"
	attr2 = "dog"

	def fun(self):
		print("I'm a", self.attr1)
		print("I'm a", self.attr2)

Rodger = Dog()
print(Rodger.attr1)
Rodger.fun()
