def add(x, y):
    a = x + y 
    print(f"The sum of {x} and {y} is {a}.")

def sub(x, y):
    s = x - y
    print(f"The subtraction of {x} and {y} is {s}.")

def multi(x, y):
    m = x * y
    return m

def div(x, y):
    d = x / y
    return d

x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
o = int(input("Choose an operator:\n1. Add\n2. Subtract\n3. Multiplication\n4. Division\nEnter an option: "))

if o == 1:
    add(x, y)
elif o == 2:
    sub(x, y)
elif o == 3:
    print(f"The multiplication of {x} and {y} is {multi(x, y)}")
elif o == 4:
    print(f"The division of {x} and {y} is {div(x, y)}")
else:
    print("Error the option doesn't exists.")