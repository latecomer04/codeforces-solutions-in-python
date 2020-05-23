s=input()
if 97<=ord(s[0])<=122:
    a=s[0]
    b=chr(ord(a)-32)
    s=b+s[1:]
    print(s)
else:
    print(s)
