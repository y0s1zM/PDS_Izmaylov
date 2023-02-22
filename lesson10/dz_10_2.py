def check_unique_numbers(numbers):
    try:
        if len(numbers) == len(set(numbers)):
            print("Усі номери в списку унікальні")
        else:
            print("У списку є повторювані номери")
    except TypeError:
        print("Не є списком чисел")
    except:
        print("Під час обробки введених даних сталася помилка")



check_unique_numbers([1, 2, 3, 4, 5])
check_unique_numbers([1, 2, 3, 4, 4])
check_unique_numbers(123)