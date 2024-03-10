import generateSelcal as genSc

while True:
    times = input("How many selcals do you want to generate? ")
    while True:
        try:
            times = int(times)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    for i in range(times):
        print(genSc.generate_selcal())
