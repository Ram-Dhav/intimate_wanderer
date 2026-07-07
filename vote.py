name = input("Hello! What is your name? ")
age = int(input(f"Hello {name}, enter your age: "))
if age < 18:
    print(f"Sorry {name}, you are not eligible to vote.")
elif age >= 18:
    print(f"Congratulations {name}, you are eligible to vote.") 

else:
    print(f"Sorry {name}, you are not eligible to vote. It may be a {type(age).__name__}.")