'''3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках'''
import random


NUM_ARR = []


for i in range(20):
  NUM_ARR.append(random.randint(0,50))
print(NUM_ARR)

def merge_sort(left, right):
  left_i = 0
  right_i = 0
  ARR = []
  while left_i < len(left) and right_i < len(right):
    if left[left_i] < right[right_i]:
      ARR.append(left[left_i])
      left_i += 1
    else:
      ARR.append(right[right_i])
      right_i += 1
  if left_i < len(left):
    ARR += left[left_i:]
  if right_i < len(right):
    ARR += right[right_i:]
  return ARR

def merge(NUM_ARR):
  if len(NUM_ARR) == 1:
    return NUM_ARR
  middle = len(NUM_ARR) // 2
  left_a = merge(NUM_ARR[:middle])
  right_a = merge(NUM_ARR[middle:])
  return merge_sort(left_a, right_a)

print('-------------------------')
print(merge(NUM_ARR))
