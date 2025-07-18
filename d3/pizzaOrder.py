print("wecome to the python pizza delivery service")
size = input("What size pizza do you want? S, M, or L: ").upper().strip()
add_pepperoni = input("Do you want pepperoni? Y or N: ").upper().strip()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper().strip()
bill = 0
if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1     
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
print(f"Your final bill is: ${bill}")