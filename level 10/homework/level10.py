# iterate over numbers from 0 to 100
for a in range(101):
    for b in range(101):
        # Perform addition
        addition = a + b
        print(f"{a} + {b} = {addition}")

        # Perform subtraction
        subtraction = a - b
        print(f"{a} - {b} = {subtraction}")

        # Perform multiplication
        multiplication = a * b
        print(f"{a} * {b} = {multiplication}")

        # Perform division if j is not zero
        if b != 0:
            division = a / b
            print(f"{a} / {b} = {division}")