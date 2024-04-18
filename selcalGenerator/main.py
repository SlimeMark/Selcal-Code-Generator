import generateSelcal as genSc

while True:
    try:
        times = input("How many selcals do you want to generate? \nCtrl+C to interrupt.\n\033[36m>>>\033[0m")
        times = int(times)
        for i in range(times):
            print("\033[32m"+genSc.generate_selcal()+"\033[0m")
    except KeyboardInterrupt:
        print("\n\033[33mConfirm? (y/n)\033[0m")
        if input().lower() == "y":
            break
    except ValueError:
        print("\033[31mInvalid input. Please enter a number.\n\033[0m")
