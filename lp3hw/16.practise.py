# practise of writing a file

from sys import argv

script, filename = argv

print(f"writing in {filename}")

print("opening file")
target = open(filename, 'w')

#target.truncate()

line = input("enter your content: ")

print(f"writing content in {filename}")

target.write(line)

print("closing file!")

target.close()

print("reading file") 
print(open(filename).read())
