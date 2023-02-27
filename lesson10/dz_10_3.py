class NegativeNumberError(Exception):

    def __init__(self, number):
        self.number = number
        self.message = f"Number {number} is negative. Only positive numbers are allowed."

    def __str__(self):
        return self.message

number = -5
if number < 0:
    raise NegativeNumberError(number)