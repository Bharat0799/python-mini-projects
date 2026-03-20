
def convert_c_to_f(c):
    return (c * 9/5) + 32
def convert_f_to_c(f):
    return (f - 32) * 5/9
def main():
    choice=input("1 c_to_f or 2 f_to_c? ")
    if choice == '1':
        c = float(input("Enter temperature in celsius: "))
        f = convert_c_to_f(c)
        print(f"fahrenheit: {f}")
    elif choice == '2':
        f = float(input("Enter temperature in fahrenheit: "))
        c = convert_f_to_c(f)
        print(f"celsius: {c}")
    else:
        print("Invalid choice")
while True:
    main()
    again = input("Do you want to convert another temperature? (y/n): ")
    if again.lower() != "y":
        break

