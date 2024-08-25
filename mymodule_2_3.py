my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
x = 0
print('Список', my_list,
      '\nположительные числа из списка:')
while x < len(my_list):
    number = my_list[x]
    x = x + 1
    if number == 0:
        continue
    elif number < 0:
        print('Встретилось отрицательное число', number)
        break

    elif x == len(my_list):
        print(number)
        print('закончился список')

    else:
        print(number)
