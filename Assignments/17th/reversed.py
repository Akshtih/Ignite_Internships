list = input().split()
revlist = []
for i in range(len(list)-1,-1,-1):
    revlist.append(list[i])
print(revlist)