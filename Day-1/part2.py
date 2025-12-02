def code_crack(file):
    with open(file, "r") as f:
        data = f.readlines()
    counter = 0
    number = 50
    previous_number = None
    for i in data:
        print(f"Previous number: {previous_number}")
        print(i)
        number += (int(i[1:]) if i.startswith("R") else -int(i[1:]))
        if  number > 99:
            print(number)
            if previous_number != 0 or number > 99:
                counter += (number // 100)
            print("counter 1+: " + str(counter))
            number = number % 100
            if number == 0:
                counter -= 1
            print(number)
        elif number < 0:
            if previous_number != 0 or number < -99:
                counter += (abs(number) // 100) + 1
            print("counter 1-: " + str(counter))
            number = number % 100
            if number == 0:
                counter -= 1
            print(number)
        if number == 0:
            counter += 1
        print("counter 2: " + str(counter))
        print("---------------------------")
        previous_number = number
    return counter

print(code_crack("test.txt"))