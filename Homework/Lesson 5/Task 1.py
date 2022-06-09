'''1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.'''
from statistics import mean
quantity = int(input('quantity of company: '))
company_profits = []
company_names = []
company_more, company_less = '', ''
for num in range(1, quantity + 1, 1):
  company_name = input('Name of company: ')
  company_names.append(company_name)
for i in range(1, quantity + 1, 1):
  company_profit = 0
  print(company_names[i - 1])
  for n in range(1, 5, 1):
    company_profit += int(input('Enter profit: '))
  company_profits.append(company_profit)
average_profit = mean(company_profits)
for m in range(1, quantity + 1, 1):
  if company_profits[m - 1] < average_profit:
    company_less += company_names[m - 1] + ' '
  else:
    company_more += company_names[m - 1] + ' '
print('More then average profit: ', company_more, '\n', 'Less then average profit: ', company_less, sep = '')