            #DZ 5
import os
    #1
# dict = {"name": "Yosya", "old": 31}
# string = "therylongstringasyousee"
#
# def new_file_function(string, dict):
#     with open(fr"{string}.txt", mode='w') as file:
#         file.write(fr"{dict}")
#     return
#
# new_file_function(string,dict)

    #2


# dict = {"name": "Yosya", "old": 31}
# string = "therylongstringasyousee"
# def new_func(string):
#     with open(fr"{string}.txt", mode='r') as file:
#         lines = (file.readlines())
#
#     dictionary = {}
#     for line in lines:
#         key, value = line.strip().split(',')
#         dictionary[key] = value
#
#
#     return dictionary
# a = new_func(string)
# print(a)

    #3

current_dir =  os.getcwd()
file_list = os.listdir(current_dir)

def new_funk(*args):
    file_count = 0
    for file_name in file_list:
        if os.path.isfile(os.path.join(current_dir,file_name)):
            file_count += 1
        print("Kilkist failiv", file_count)
        print(file_name)

new_funk()