name = input("Hello! What is your name? ")
a = float(input(f"Hello {name}, enter the number you wish to be declared as odd or even: "))
if a % 2 == 0:
    print(f"The number {a} is even")
elif a % 2 != 0:
    print(f"The number {a} is odd")

else:
    print(f"The number {a} is neither odd nor even, {name}")

