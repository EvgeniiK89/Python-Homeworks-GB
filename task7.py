#7. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
a = int(input("Результат пробежки в первый день в км: "))
b = int(input("Требуемый результат спортсмена в км: "))

#Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

running_days = 1
first_day_distance = a
while first_day_distance < b:
        a = a + 0.1 * a
        running_days += 1
        first_day_distance = first_day_distance + a
print(f"Требуемый результат будет достигнут на %.d день" % running_days)