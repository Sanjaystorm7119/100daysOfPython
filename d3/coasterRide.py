height = input("Enter your height in centimeters : ")
bill =0

if int(height) < 120:
    print("You can't ride the coaster, sorry!")
else:
    age = int(input("Enter your age : "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? (Y/N) : ").strip().upper()
    if wants_photo == 'Y':
        bill += 3

print(f"Your total bill is: ${bill}")