# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

candy1 = items[0:9] #slice out "Bubblegum"
candy2 = items[11:20] #slice out "Chocolate"
dry_goods = items[22:27] #slice out "Pasta"

category1 = categories[0:11] #slice out "Candy Aisle"
category2 = categories[13:24] #slice out "Pasta Aisle"

bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"

print("We have " + candy1.lower() + " for " + bubblegum_price + " in the " + category1)
print("We have " + candy2.lower() + " for " + chocolate_price + " in the " + category1)
print("We have " + dry_goods.lower() + " for " + pasta_price + " in the " + category2)