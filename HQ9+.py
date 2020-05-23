def lang():
    p=input()
    ref="HQ9"
    for i in ref:
        if i in p:
            return "YES"
    return "NO"
print(lang())

