s = input().strip().upper()
st = ""
for i in s:
    if i not in [' ', ',', '.', '!', '?','-']:
        st += i
print(st)
print(st == st[::-1])