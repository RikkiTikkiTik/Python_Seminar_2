# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть. Количество монет и их положение (0 или 1) пользователь вводит с клавиатуры.
# Примеры/Тесты:
# Введите кол-во монет>? 5
# Положение монеты 0: 0 или 1>? 1
# ...
# 1 0 1 1 0
# Кол-во монет, чтобы перевернуть: 2
counter_0 = 0
counter_1 = 0
coin_quantity = int(input('Введите количество монет: '))
for i in range(coin_quantity) :
    coin_side = int(input(f'Положение монеты {i}: 0 или 1? '))
    if coin_side== 0:
        counter_0 += 1
    else:
        counter_1 += 1
print(f'Кол-во монет, чтобы перевернуть: {min(counter_0, counter_1)}')