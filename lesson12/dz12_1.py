
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    nums = [100, 500, 1000, 2000, 5000, 10000, 20000]

    # Запуск задач в ThreadPoolExecutor
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(factorial, nums)
    end_time = time.time()
    print(f"Час виконання задач в ThreadPoolExecutor: {end_time - start_time} секунд")

    # Запуск задач в ProcessPoolExecutor
    start_time = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = executor.map(factorial, nums)
    end_time = time.time()
    print(f"Час виконання задач в ProcessPoolExecutor: {end_time - start_time} секунд")

if __name__ == "__main__":
    main()
