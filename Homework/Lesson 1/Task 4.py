import random
print('Enter start diapazon')
a=float(input())
print('Enter end diapazon')
b=float(input())
r1=random.uniform(a,b)
r2=random.randint(a,b)
print(r1,r2)