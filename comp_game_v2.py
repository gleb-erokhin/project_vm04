import random                       # импортируем модуль random

min_number = 1                      # вводим переменные для значений
max_number = 100                    # максимум и минимум
# для того чтобы зайти в цикл присваевам переменной None
result = None

# начинали писать цикл while True, но решили его улучшить чтобы убрать бесконечность
while result != '=':                # цикл выполняется пока результат не равен =
    # в переменную возьме запишем случайное число от 1 до 100
    number = random.randint(min_number,max_number)
    # компьютер предлягает случайное число - печатаем и смотрим его
    print(number)
    # просим ответить пользователя равно больше или меньше выбранное число
    result = input('число верно =, число больше >, число меньше < ')
    if result == '>':               # тут указываем больше чем загаданное
        min_number = number + 1     # укажем что делать если число больше
    elif result == '<':             # тут указываем меньше чем загаданное
        max_number = number - 1     # укажем что делать если число меньше
print('Победа')  # за счет того что установили другое условие while отличное от True
# меняем выход из цикла по break, и убираем вывод - Верно вне цикла while
# тут написали код примерный для работы, для того чтобы писать удобно, надо писать по частям



