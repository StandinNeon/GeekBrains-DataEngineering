'''
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
import random
N = 100
A = [0] * N
max = 0
k1 = N
for i in range(0, N, 1):
  A[i] = random.randint(0, N)
  if A[i] >= max:
    max = A[i]
  if A[i] <= min:
    min = A[i]
print(A, max, min)
for n in range(0, N, 1):
  if A[n] == max:
    A[n] = min
  elif A[n] == min:
    A[n] = max
print(A)
