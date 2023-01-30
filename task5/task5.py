"""5. Создать (программно) текстовый файл, записать в него программно набор
чисел, разделённых пробелами. Программа должна подсчитывать сумму чисел в
файле и выводить её на экран."""

def addition():

        with open('task_5.txt', 'w+') as file_numb:
            line = input('Введите числа: \n')
            file_numb.writelines(line)
            number = line.split()

            print(sum(map(int, number)))

addition()