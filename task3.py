# 3.Узнайте у пользователя число n

n = int(input('Введите число: '))

# Найдите сумму чисел n + nn + nnn.

str_n = str(n)
n2 = str_n + str_n
n3 = str_n + str_n + str_n
total = n + int(n2) + int(n3)
print("Сумма всех чисел:", total)