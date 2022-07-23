
print("Welcome to Calculator!")
num1 = int(input("Insert a number: "))
num2 = int(input("Insert a number: "))

print("Which Operation?")
ope = str(input("Sum(+) Sub(-) Mult(*) Div(/): "))

if ope == "+":
    res = num1 + num2
elif ope == "-":
    res = num1 - num2
elif ope == "*":
    res = num1 * num2
elif ope == "/":
    res = num1 / num2
    
print(f"Result: {res}")
