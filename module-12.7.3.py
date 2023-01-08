Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> money = int(input("Введите сумму которую инвестируете:"))
Введите сумму которую инвестируете:100000
>>> per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
>>> procent = list(per_cent.values())
>>> bankTKB = round(procent[0]/100*money)
>>> bankCKB = round(procent[1]/100*money)
>>> bankVTB = round(procent[2]/100*money)
>>> bankSBER = round(procent[3]/100*money)
>>> deposit = [bankTKB, bankCKB, bankVTB, bankSBER]
>>> print("Возможный доход:", deposit)
Возможный доход: [5600, 5900, 4280, 4000]
>>> deposit.max()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    deposit.max()
AttributeError: 'list' object has no attribute 'max'
>>> deposit.sort()
>>> print("Максимальная сумма, которую вы можете заработать - ", deposit[-1])
Максимальная сумма, которую вы можете заработать -  5900
