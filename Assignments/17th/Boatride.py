n = int(input())
list = []
for i in range(n):
    list.append(input())

list.sort()
for i in range(len(list)):
    print(list[i])