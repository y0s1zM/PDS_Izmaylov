from multiprocessing import Pool
import os

def f(x):
    return x*x
if __name__ == '__main__':
    cpu = os.cpu_count()
    print(cpu)
