import math

num = float(input("Enter a number: "))

if num > 0:
    print(f"The number {num} is positive")
elif num < 0:
    print(f"The number {num} is negative")
elif num == 0:
    print(f"The number {num} is zero")
else:
    print(f"The number {num} is neither positive, negative, nor zero. It may be a {type(num).__name__}.")
    

print(f"Pi = {math.pi}")
print(f"Square root of 2 = {math.sqrt(2)}")

