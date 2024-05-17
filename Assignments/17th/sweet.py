
list1 = []
name = input()
while name != "":
    list1.append(name)
    name = input()

d = {}
set1 = list(set(list1))
for i in range(len(list1)):
    if list1[i] in d:
        d[list1[i]] += 1
    else:
        d[list1[i]] = 1
        
for i in range(len(d)):
    print(set1[i],":",d[set1[i]])
