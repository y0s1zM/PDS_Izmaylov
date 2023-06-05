#1
def last_lines(path):
    with open(path, mode= 'r') as file:
        rows = 0
        ml = []
        for f in file:
            ml.append(f)
            rows += 1
    print(ml[rows - 2])
    print(ml[rows - 1])

last_lines('test.txt')