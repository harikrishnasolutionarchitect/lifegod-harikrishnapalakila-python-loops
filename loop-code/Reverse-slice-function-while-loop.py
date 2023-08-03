s="Hari"
""" r=s[::-1]
print(r) """


""" r=reversed(s)
r1=''.join(r)
print(r1) """

r=''
i=len(s)-1
while i >= 0:
    r = r+s[i]
    i = i-1
    print(r)