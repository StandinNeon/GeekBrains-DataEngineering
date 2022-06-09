"''
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"''
print('Enter 3 digit number: ')
put = int(input())
hundreds = put // 100
tens = (put // 10) - (hundreds * 10)
units = put - ((hundreds * 100) + (tens * 10))
summa=hundreds+tens+units
product=hundreds*tens*units
print('Sum of digits:',summa)
print('Product of digits:',product)
