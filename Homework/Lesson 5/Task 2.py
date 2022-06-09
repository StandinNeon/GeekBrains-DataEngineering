'''2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].'''

from collections import deque 

summa_f = 0
summa_s = 0
alphabet = []
arr_summa = []
arr_multi = []
b = 48
print('Сложение и умножение шестнадцатеричных чисел')
first = deque(input('Первое число: '))
second = deque(input('Второе число: '))
first.reverse()
second.reverse()

for n in range(65, 71):
  while b <= 57 and n <= 65:
    alphabet.append(chr(b))
    b += 1
  alphabet.append(chr(n))

if len(first) > len(second):
  max_len =  len(first) 
else:
  max_len = len(second) 

for i in range(0, max_len, 1):
  summa_f += int(first[i], base = 16) \
    * 16**first.index(first[i])
  summa_s += int(second[i], base = 16) \
    * 16**second.index(second[i])
summa = summa_f + summa_s 
summa_del = summa

for sum in range(0, len(str(summa))):
  summa_ost = summa_del % 16
  summa_del = summa_del // 16
  arr_summa.append(alphabet[summa_ost])
arr_summa.reverse()
print('Сумма:', arr_summa)

multi = summa_f * summa_s 
multi_del = multi
for sum in range(0, len(str(multi))):
  multi_ost = multi_del % 16
  multi_del = multi_del // 16
  arr_multi.append(alphabet[multi_ost])
arr_multi.reverse()
print('Произведение:',arr_multi)