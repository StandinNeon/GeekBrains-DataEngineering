'''3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках'''
import random


NUM = []
LEFT = []
RIGHT = []
med = 0
lines = 3
columns = (2 * lines) + 1
if lines > columns:
    lines, columns = columns, lines

#Генерация массива NUM
NUM = [[random.randint(1, 10) for j in range(columns)] \
for i in range(lines)]
print(NUM)

#Нахождение медианы med
for row in NUM: 
  med += sum(row) 
med = med / (lines * columns)

#Деление массива на две части
def matrix_spliting(NUM, med):
    for column in range(len(NUM)):
        for line in range(len(NUM)):
            if NUM[column][line] < med:
                LEFT.append(NUM[column][line])
            else:
                RIGHT.append(NUM[column][line])
    return LEFT, RIGHT


print('Медиана:', round(med, 1), matrix_spliting(NUM, med))