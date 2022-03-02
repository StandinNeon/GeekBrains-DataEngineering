procn =[]
enc = ['11','12','13','14','15','16','17','18','19']
for i in range(1, 101, 1):
    procn.append(str(i))
for N in procn:
    if N[-1] == '1' and N not in enc:
        print(f'{N} процент')
    elif N[-1] in ('2','3','4') and N[0] != '1':
        print(f'{N} процента')
    else:
        print(f'{N} процентов')