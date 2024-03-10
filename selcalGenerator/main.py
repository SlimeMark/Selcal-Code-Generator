import generateSelcal as genSc

while True:
    times = input("How many selcals do you want to generate? ")
    try:
        times = int(times)
        for i in range(times):
            print(genSc.generate_selcal())
    except ValueError:
        print("Invalid input. Please enter a number.")
