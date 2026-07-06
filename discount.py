marked_price = float(input("Enter the marked price:"))
discount_percentage = float(input("Enter the discount percentage:"))
discount = (marked_price * discount_percentage) / 100
if discount_percentage > 100:
    print("The discount cannot be calculated, since the discount percentage cannot be more than 100%")

elif discount_percentage < 100:
    final_amount = (marked_price - discount)
    print("The discount is: " , discount)
    print("The final amount after applying discount is, $" , final_amount)