'''
Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
'''

print('Введите значение выручки фирмы')
revenue = int(input())
print('Введите значение издержек фирмы')
cost = int(input())
profit = revenue - cost
if profit > 0:
    print('Фирма отработала с прибылью')
    print(f'Рентабельность фирмы составила: {profit/cost:.2f}')
elif profit == 0:
    print('Фирма отработала в ноль')
elif profit < 0 :
    print('Фирма отработала в убыток')
print('Введите численность фирмы')
staff_number = int(input())
print(f'Прибыль на 1 сотрудика составила: {profit/staff_number:.2f}')
