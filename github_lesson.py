a = [65,76,87,98,65]
index = 0
max = 0
index_max_number = index
while index < len(a):
    if max < a[index]:
        max = a[index]
        index_max_number = index
    index += 1
print(max)
print(index_max_number)



a = [65,76,87,98,65,6565,88,-2,-1]
index = 0
min = a[0]
index_min_number = index
while index < len(a):
    if min > a[index]:
        min = a[index]
        index_min_number = index
    index += 1
print(min)
print(index_min_number)
