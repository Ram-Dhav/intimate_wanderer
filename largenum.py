name = input("Hello! What is your name? ")
a = int(input(f"Hello {name}, enter the first number: "))
b = int(input(f"Hello {name}, enter the second number: "))

if a > b:
    print(f"The number {a} is greater")
elif a < b:
    print(f"The number {b} is greater")
else:
    print(f"Both the numbers {a} and {b} are equal, {name}")

