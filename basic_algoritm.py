#max_number,max_index_number
a = [65,76,87,98,65]
index = 0
max = 0
index_max_number = index
while index < len(a):
    if max < a[index]:
        max = a[index]
        index_max_number = index
    index += 1
print(f"большее число в массиве: {max}")
print(f"индекс большего числа в массиве: {index_max_number}")



#min_number,min_index_number
a = [65,76,87,98,65,6565,88,-2,-1]
index = 0
min = a[0]
index_min_number = index
while index < len(a):
    if min > a[index]:
        min = a[index]
        index_min_number = index
    index += 1
print(f"меньшее число: {min}")
print(f"индекс меньшегго чиисла: {index_min_number}")




#Среднее арифметическое среди всех чисел массива
a = [54465,767,87,98,656,87,989,56]
sum = 0
index = 0
while index < len(a):
    sum = sum + a[index]
    index += 1
print(f"среднее арефметическое: {sum/len(a)}")




#Возведение каждого числа в массиве в квадрат,сумма всех получившихся чисел
a = [76,76,8798,567,6587,98]
index = 0
sum = a[index]
while index < len(a):
    sum = sum + (a[index]^2)
    index += 1
print(f"сумма квадратов всего массива: {sum}")


#Задача про собаку и двух друзей,алгоритм решения
distance = 10000
first_friend_speed = 10
second_friend_speed = 20
dog_speed = 40
friend = 2
count = 0
while distance > 10:
    if friend == 1:
        time = distance/(dog_speed + first_friend_speed)
        friend = 2
        distance = distance - (first_friend_speed + second_friend_speed) * time
        count += 1
    elif friend == 2:
        time = distance / (dog_speed + second_friend_speed)
        friend = 2
        distance = distance - (first_friend_speed + second_friend_speed) * time
        count += 1
print(f"собака пробежит: {count} раз")