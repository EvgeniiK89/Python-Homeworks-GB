"""2.Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке."""

file2 = open('ТЗ_2.txt', 'r')
content = file2.read()
print(f'Произвольный текст: \n {content} \n')

file2 = open('ТЗ_2.txt', 'r')
content = file2.readlines()
print(f'Кол-во строк: \n {len(content)}')

file2 = open('ТЗ_2.txt', 'r')
content = file2.read()
content = content.split()
print(f'Кол-во слов: \n {len(content)}')
file2.close()
