# Fucntions and variables

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes_of_crackers!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

print("OR, we can just give the function numbers directly:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print("math inside function")
cheese_and_crackers(10+25, 5+6)

print("add varibles with new values")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

 
