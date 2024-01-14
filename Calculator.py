print("\tCalculator\n")
print("Acessable operations are :\n1. add(a)\n2. substract(s)\n3. multiplication(m)\n4. division(d)\n5. power(p)\n")
char = input("Enter your choice : ")
if(char == "a" or char == "add"):
    print("You have choosen Addition")
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    num3 = num1 + num2
    print(f"The sum of {num1} and {num2} is equal to {num3}")
elif(char == "s" or char == "substract"):
    print("You have choosen substraction")
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    if(num1>num2):
        num3 = num1 - num2 
        print(f"The substraction of {num1} and {num2} is equal to {num3}")
    else:
        num3 = num2 - num1
        print(f"The substraction of {num2} and {num1} is equal to {num3}")
elif(char == "m" or char == "multiplication"):
    print("You have choosen Multiplication")
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    num3 = num1 * num2
    print(f"The multiplication of {num1} and {num2} is equal to {num3}")
elif(char == "d" or char == "division"):
    print("You have choosen Division")
    num = int(input("Enter the numerator number : "))
    deno = int(input("Enter the denominator number : "))
    num3 = num/deno
    print(f"The number {num} divided by {deno} is equal to {num3}")
elif(char == "p" or char == "power"):
    print("You have choosen Power")
    base = int(input("Enter the base number : "))
    exponent = int(input("Enter the power number : "))
    num3 = base ** exponent
    print(f"The number {base} raised to power of {exponent} is equal to {num3}")
else:
    print("The character or string you entered is not in any choice mentioned.")