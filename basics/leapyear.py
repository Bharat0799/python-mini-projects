num = int(input("Enter a year: "))
if num % 4 == 0:
    if num % 100 == 0:
        if num % 4000 == 0:
            print(f"{num} is a leap year.")
        else:
            print(f"{num} is not a leap year.")
    else:
        print(f"{num} is a leap year.")
else:
    print(f"{num} is not a leap year.")