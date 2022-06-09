a='y='
a1=''
a2='x'
a3=''
b=0
print('Enter X1:')
X1=int(input())
print('Enter Y1:')
Y1=int(input())
print('Enter X2:')
X2=int(input())
print('Enter Y2:')
Y2=int(input())
if (X1 != X2):
  k=(Y1-Y2)/(X1-X2)
else:
  a1=''
b=(Y2)/(1+(X2*Y1/X1))
if (b<0):
  a3=''
if (b==0):
  a3=''
if (b>0):
  a3='+'

print('Your equation:',a,a1,a2,a3,b,sep='')