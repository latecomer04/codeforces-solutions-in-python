
def chat():
    s=input()
    refer="hello"
    i=0
    for j in range(len(s)):
        if s[j]==refer[i]:
            i=i+1
        if i==5:
            return "YES"
    return "NO"
print(chat())
