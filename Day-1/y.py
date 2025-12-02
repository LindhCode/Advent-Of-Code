def code_crack(file):
    with open(file, "r") as f:
        data = f.read().splitlines()

    position = 50
    count = 0

    for line in data:
        direction = -1 if line[0] == "L" else 1
        amount = int(line[1:])
        
        # Flytta vredet
        position = (position + direction * amount) % 100
        
        # Om vredet stannar på 0 -> öka räknaren
        if position == 0:
            count += 1

    return count


print(code_crack("data.txt"))