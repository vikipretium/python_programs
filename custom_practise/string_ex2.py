def myfunc(st):
return ''.join([st[i].lower() if i%2==0 else st[i].upper() for i in range(len(st))])

