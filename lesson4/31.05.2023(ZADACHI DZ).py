
                    #dz nomer 4, ZADACHKI
    #1
# def my_function(*args):
#     flag = True
#     for i in args:
#         if not isinstance(i, str):
#             flag = False
#             break
#     return flag
#
# st = my_function("sdfewq", "sds", "sdwqd", "dsad")
# print(st)
    #2
# import math
# def kvadrat(*args):
#     x = int(input("Vvedit dovzhinu storonu kvadrata v cm: "))
#     return print(f"Plosha kvadrata: {x * x} santimetrov\nPerimetr kvadrata: {x * 4} santimetrov\nDiagonal kvadrata: {math.sqrt(2) * x} santimetrov")
#
# kvadrat()
    #2variant 2
# def kvad(st):
#     Plosha = st * st
#     Perimetr = st * 4
#     Diagonal = 2 ** 0.5 * st
#     answer = [Plosha, Perimetr,Diagonal]
#     return answer
#
# s = kvad(5)
# print(s)
    #3
# def up_to_100(up):
#     if up < 100:
#         up += 1
#     if up < 100:
#         print(up)
#         up_to_100(up)
#     else:
#         print(up)
#
# up_to_100(57)
    #4
# def join_list(list1, list2):
#     return list1 + list2
#
# a = [1,2,3]
# b = [3,4,5]
# x = join_list(a,b)
#
# print(x)




























