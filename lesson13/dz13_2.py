import random
import time

def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j] < lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j -= 1
    return lst

def average_sort_time(lst, iterations=10):
    total_time = 0
    for i in range(iterations):
        start_time = time.time()
        sorted_lst = insertion_sort(lst.copy())
        end_time = time.time()
        total_time += end_time - start_time
    return total_time / iterations

int_list = [random.randint(0, 1000) for _ in range(5000)]
float_list = [round(random.uniform(0.1, 100.0), 2) for _ in range(5000)]
str_list = ["".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=random.randint(1, 10))) for _ in range(5000)]

int_sort_time = average_sort_time(int_list)
float_sort_time = average_sort_time(float_list)
str_sort_time = average_sort_time(str_list)

print(f"Average sort time for int_list: {int_sort_time}")
print(f"Average sort time for float_list: {float_sort_time}")
print(f"Average sort time for str_list: {str_sort_time}")