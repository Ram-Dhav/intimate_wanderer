numlist = input("What numbers do you want to be added together? ")
numbers = numlist.split()

sum_value = 0
for number in numbers:
    sum_value = sum_value + int(number)

print("sum is:", sum_value)
