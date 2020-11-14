    #var and names

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
car_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("Number of availble cars",cars)
print("Drivers availble:",drivers)
print("unused cars:",car_not_driven)
print("people can transport today:",carpool_capacity)
print("total passengers:",passengers)
print("each car passengers:",average_passengers_per_car)

