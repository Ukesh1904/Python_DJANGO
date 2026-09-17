x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
o = int(input("Operators:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\nChoose an option: "))

if o == 1:
    a = x + y 
    print(f"The addition of {x} and {y} is {a}.")
elif o == 2:
    s = x - y
    print(f"The subtraction of {x} and {y} is {s}.")
elif o == 3:
    m = x * y
    print(f"The multiplication of {x} and {y} is {m}.")
elif o == 4:
    d = x/y
    print(f"The division of {x} and {y} is {d}.")
else:
    print("Error! Option doesn't exists.")