print("Basket Cost =")
customer_basket_cost = float(input(""))  
print("Basket Weight =")
customer_basket_weight = float(input("")) 

shipping_cost = 0
if customer_basket_cost >= 100:
    shipping_cost = 0
else:
    shipping_cost = customer_basket_weight * 1.2  

total_cost = shipping_cost + customer_basket_cost
print("Total Cost =", total_cost)
