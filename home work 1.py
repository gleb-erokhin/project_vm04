# HW1
#number = int(input('Введите число: '))
#print(number + 2)

# HW2
#number = int(input('Введите число от 0 до 10 (не включительно): '))
#while 10 < number > 0:
#    print('Введено не верное число')
#    number = int(input('Введите число от 0 до 10 (не включительно): '))
#else:
#    print(number ** 2)

# HW3
#Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
#Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
#Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# этот вариант тоже не прошел, срабатывает только второй блок при выборе 41 год и 121 кг, хотя в нем возраст
#указан не более 40 лет.

name = 'Вася'
sur_name = 'пупкин'
age = int(input('Введите Возраст: '))
veight = int(input('Введите Вес: '))
if age < 30 and 50 < veight < 120:
    print(name, age, 'год, ', 'вес', veight, '- Вы в хорошем состоянии')
elif age < 40 and veight < 50 or veight > 120:
    print(name, age, 'год, ', 'вес', veight, '- Вам следует заняться собой')
elif age > 40 and veight < 50 or veight > 120:
    print(name, age, 'год, ', 'вес', veight, '- Вам требуется врачебный осмотр')