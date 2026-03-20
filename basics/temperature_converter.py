choice=input("convert (1) celsius to fahrenheit or (2) fahrenheit to celsius? ")
if choice == '1':
    c = float(input("Enter tempture in celsius: "))
    f = (c * 9/5) +32
    print(f"fahrenheit: {f}")
elif choice == '2':
    f = float(input("Enter temperature in fahrenheit: "))
    c = (f - 32) * 5/9
    print(f"celsius: {c}")
else:
    print("Invalid choice")