substrings = sorted(list(map(str, input().split())), key=len, reverse=True)

if substrings.__len__() > 1:
    result = substrings[0] + "-" + substrings[1]
elif substrings.__len__() > 0:
    result = substrings[0]
else:
    result = "There is no words"
print(result)
