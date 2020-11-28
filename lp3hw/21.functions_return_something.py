# Functions return something

def add(a,b):
    print(f"Adding {a} + {b}")
    return a + b

def sub(a,b):
    print(f"sub {a} - {b}")
    return a - b

def mul(a,b):
    print(f"mul {a} * {b}")
    return a * b

def div(a,b):
    print(f"div {a} / {b}")
    return a / b


print("lets do some math")

age = add(30,5)
height = sub(78,4)
weight = mul(90,2)
iq = div(100,2)

print(f"Age: {age}, Height: {height} , Weight: {weight} , iq: {iq}")

print("Puzzle")

what = add(age, sub(height,mul(weight,div(iq,2))))

print("ans: ",what, " some odd ans!")


