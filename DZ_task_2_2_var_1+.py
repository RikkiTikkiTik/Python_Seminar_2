# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# Примеры/Тесты:
# 4 4 -> 2 2
# 5 6 -> 2 3
# Вариант 1. Здесь нужно составить два уравнения. Которые приведут к квадратному уравнению.
import math # Импортируем библиотеку Math
sum = int(input('Сумма загаданных чисел: '))
multiple = int(input('Произведение загаданных чисел: '))
# x + y = sum
# x * y = multiple
# y = sum - x
# x * (sum - x) = multiple
# x*sum - x**2 = multiple
# x**2 -sum*x + multiple = 0
D = sum**2 - 4 * multiple
if D < 0 :
    print ('Петя лукавит =)')
elif D == 0 :
    x_1 = sum / 2
    x_2 = x_1
    print(f'{max(x_1, x_2)} {sum - max(x_1, x_2)}')
else :
    x_1 = (sum + math.sqrt(D))/2 # используем библиотеку Math
    x_2 = (sum - math.sqrt(D))/2
    print(f'{max(x_1, x_2)} {sum - max(x_1, x_2)}')