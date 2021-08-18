# Расчет банковского процента
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму:"))
print('Расчитаем годовой процент по депозиту')
deposit1 = money * per_cent['ТКБ'] / 100
deposit2 = money * per_cent['СКБ'] / 100
deposit3 = money * per_cent['ВТБ'] / 100
deposit4 = money * per_cent['СБЕР'] / 100
deposit = [deposit1, deposit2, deposit3, deposit4]
print(deposit)
max_deposit = max(deposit)
print("Максимальная сумма, которую Вы можете заработать -", max_deposit)

