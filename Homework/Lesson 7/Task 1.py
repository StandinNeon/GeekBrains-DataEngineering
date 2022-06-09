'''1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее)'''
import random


NUM_ARR = []

for i in range(50):
  NUM_ARR.append(random.randint(-100,100))
print(NUM_ARR)

def bubble_sort(NUM_ARR):
  j = 1
  while j < len(NUM_ARR):
    for i in range(len(NUM_ARR)-j):
      if NUM_ARR[i] > NUM_ARR[i+1]:
        NUM_ARR[i], NUM_ARR[i+1] = NUM_ARR[i+1], NUM_ARR[i]
    j += 1
  return NUM_ARR


print('--------------------------------')
print(bubble_sort(NUM_ARR))