num = 1
odd_num_list = []
summa = 0
esum = 0
summa_17 = 0
while num < 1000:
    if num % 2 != 0:
        odd_num_list.append(num**3)
#1.1
        list_num = list(str(odd_num_list[-1]))
        summa_num = 0
        for n in list_num:
            summa_num += int(n)
        if summa_num % 7 == 0:
            summa += odd_num_list[-1]
#1.2
        tnum = odd_num_list[-1]
        nsum = 0
        while tnum != 0:
            nsum = nsum + (tnum % 10)
            tnum = tnum // 10
        if nsum % 7 == 0:
            esum += odd_num_list[-1]
#2
        odd_num_list[-1] += 17
        list_num = list(str(odd_num_list[-1]))
        summa_num = 0
        for n in list_num:
            summa_num += int(n)
        if summa_num % 7 == 0:
            summa_17 += odd_num_list[-1]

    num += 1

print(summa, esum, summa_17)