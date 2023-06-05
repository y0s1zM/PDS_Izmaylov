    #1
# def last_lines(path):
#     with open(path, mode= 'r') as file:
#         rows = 0
#         ml = []
#         for f in file:
#             ml.append(f)
#             rows += 1
#     print(ml[rows - 2])
#     print(ml[rows - 1])
#
# last_lines('test.txt')

    #2

# numbers = list(range(101))
# list = [num for num in numbers if num % 5 == 0]
# def new_file_function(list):
#     with open("new_file.txt", mode='w') as file:
#         file.write(fr"{list}")
#     return
#
# new_file_function(list)