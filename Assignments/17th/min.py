list = list(map(int, input().split()))

min = list[0]
max = list[0]

for i in range(1, len(list)):
    if list[i] < min:
        min = list[i]
    if list[i] > max:
        max = list[i]

print("Min:", min)
print("Max:", max)