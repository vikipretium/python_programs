# file access using function

from sys import argv

script, file1 = argv

def print_all(a):
    print(a.read())

file1_opened = open(file1)


print_all(file1_opened)

