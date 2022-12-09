def months_name(month_numb):
    months = {1: 'Січень', 2: 'Лютий', 3: 'Березень', 4: 'Квітень',
              5: 'Травень', 6: 'Червень', 7: 'Липень', 8: 'Серпень',
              9: 'Вересень', 10: 'Жовтень', 11: 'Листопад', 12: 'Грудень'}
    try:
        return months[int(month_numb)]
    except KeyError as ex:
        return 'Такого місяця не існує. Введіть в діапазоні від 1го до 12ти'
    except ValueError as ex:
        return "Ви ввели не вірний символ. Введіть цифру"



a = input("Введіть номер місяця: ")
print(months_name(a))
