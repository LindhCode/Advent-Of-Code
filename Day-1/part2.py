def code_crack(file):
    with open(file, "r") as f:
        data = f.readlines()
    counter = 0
    number = 50
    passed_border = False
    for i in data:

        number += (int(i[1:]) if i.startswith("R") else -int(i[1:]))
        if  number > 99:
            #print(number)
            passed_border = True
            counter += (number // 100)
            print(number)
            number = number % 100
            print(f"Over 99: {counter}")
        elif number < 0:
            passed_border = True
            #counter += 1
            counter += (abs(number) // 100)

            number = number % 100
            print(f"Under 0: {counter}")
        if number == 0:
            counter += 1

        passed_border = False
    return counter

def correct_count_number(number, counter):
    pass

print(code_crack("test.txt"))