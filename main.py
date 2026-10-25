a = int(input())
b = int(input())

# Находим первое чётное число начиная с 'a'
start = a if a % 2 == 0 else a + 1

# Идем от start до b включительно с шагом 2
for i in range(start, b + 1, 2):
    print(i, end=" ")