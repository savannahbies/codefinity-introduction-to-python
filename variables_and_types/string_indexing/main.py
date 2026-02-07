grocery_item = "Grilled Chicken Salad"

#Find the length of the string, which includes spaces
length_of_item = len(grocery_item) #includes spaces in the count

first_char = grocery_item[0] # 'G'
second_char = grocery_item[8] # 'C'
third_char = grocery_item[16] # 'S'

last_char1 = grocery_item[-1] # 'd'
last_char2 = grocery_item[-7] # 'n'
last_char3 = grocery_item[-15] # 'd'

# Testing
print("Length of item name:", length_of_item)
print("First character of each word:", first_char, second_char, third_char)
print("Last character of each word:", last_char1, last_char2, last_char3)