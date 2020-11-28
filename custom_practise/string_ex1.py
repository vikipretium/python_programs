#even caps and odd lower.

def myfun(args):
    list1 = list(args) 
    c = ''
    for a in range(len(list1)):
        if a%2==0:
            list1[a]=list1[a].lower()
        else:
            list1[a]=list1[a].upper()
            
    d=c.join(list1)
    print(d)

myfun('abcdefgh')

def myfun1(args):
    string1 = ''
    for a in range(len(args)):
        if (a+1)%2==0:
            string1 += args[a].upper()
        else:
            string1 += args[a].lower()
    return string1
print(myfun1('abcdef'))

def myfun2(args):
    new_list = []
    for letter in range(len(args)):
        if letter % 2 == 0:
            new_list.append(args[letter].lower())
        else:
            new_list.append(args[letter].upper())

    return ''.join(new_list)

print(myfun2('abcdefghijkl'))
