
def code_crack(file):
    with open(file, "r") as f:
        data = f.readlines()
    counter = 0
    number = 50
    for i in data:
        number += (int(i[1:]) if i.startswith("R") else -int(i[1:]))
        if number < 0:
            number = number % 100
        elif number > 99:
            number = number % 100
        if number == 0:
            counter += 1
    return counter

print(code_crack("data.txt"))