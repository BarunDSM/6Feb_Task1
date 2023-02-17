def encrypt(s):
    l=list(s.lower())
    for x in range(len(l)):
        if ord(l[x])>=97:
            l[x]=chr(219-ord(l[x]))
        if l[x]==' ':
            l[x]='$'
    return "".join(l)

st="I want to become a Data Scientist."

print(encrypt(st))