import random

int_list = [random.randint(0, 1000) for _ in range(5000)]
float_list = [round(random.uniform(0.1, 100.0), 2) for _ in range(5000)]
str_list = ["".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=random.randint(1, 10))) for _ in range(5000)]

print(int_list)
print(float_list)
print(str_list)