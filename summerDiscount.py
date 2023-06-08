#a function to calculate the discount of the most expensive item in a list of products then return the total price
def calculate_total_price(prices, discount):
# check if the list of the prices is empty of None
    if not prices or len(prices) == 0:
        return 0
    else:
        max_price = max(prices)
        discount_max_price = (max_price * discount) // 100
        total_price = sum(prices) - discount_max_price
        return total_price

#exemple
print(calculate_total_price([10, 100], 20))
 