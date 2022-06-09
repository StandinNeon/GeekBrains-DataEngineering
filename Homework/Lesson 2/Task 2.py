'''
2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''
chet = 0
nechet = 0
num = input('Введите натуральное число: ')
numbs = [num[i:i+1] for i in range(0, len(num), 1)]
for i in range(0, len(num), 1):
  if int(numbs[i]) % 2 != 0:
    nechet += 1
  else:
    chet += 1
  if int(numbs[i]) == 0:
    chet += -1
print("Чётных:", chet, "Нечётных:", nechet)