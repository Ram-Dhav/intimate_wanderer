cost_price = float(input("Hello! Enter the cost price: "))
selling_price = float(input("Hello! Enter the selling price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Since the selling price is higher than the cost price, the profit is:", profit)
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("Since the selling price is lower than the cost price, the loss is:", loss)
else:
    print("Since the selling price is equal to the cost price, there is no profit and no loss.")