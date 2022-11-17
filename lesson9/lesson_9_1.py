class MyAuto:
    def __init__(self, car_model ='', colour = '', vehicle = 0):
        self.car_model = car_model
        self.colour = colour
        self.vehicle = vehicle

    def go_vpered(self):
        return print(f"{self.colour} {self.car_model} V{self.vehicle} їде вперед")
    def go_nazad(self):
        return print(f"{self.colour} {self.car_model} V{self.vehicle} їде назад")

class MyAuto2(MyAuto):

    def go_right(self):
        return print(f"{self.colour} {self.car_model} V{self.vehicle} їде направо")
    def go_left(self):
        return print(f"{self.colour} {self.car_model} V{self.vehicle} їде наліво")

car = MyAuto2("Renault Clio", "Сіре", 1.4)
car.go_vpered()
car.go_nazad()
car.go_right()
car.go_left()