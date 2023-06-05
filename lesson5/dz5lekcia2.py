    #1

# def lines_count(path):
#     with open(path, mode='r') as file:
#         rows = 0
#         for f in file:
#             rows += 1
#     print(rows)
#
# lines_count('test.txt')

    #2
import os

current_dir =  ('C:/Users/')
filelist = os.listdir(current_dir)

def file_list(*args):
    filelist = os.listdir(current_dir)
    print(filelist)

file_list(current_dir)
