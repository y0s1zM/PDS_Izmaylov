class Parallelogram:

    def __init__(self, length = 0, width = 0):
        self.__length = length
        self.__width = width

    def get_area(self):
        return self.__length * self.__width

    @property
    def length(self):
        return self.__length


class Square(Parallelogram):

    def get_area(self):
        return super().length **2



a = Parallelogram(2, 4)
print("Площа Parallelogram:", a.get_area())

b = Square(4)
print("Площа Square:", b.get_area())