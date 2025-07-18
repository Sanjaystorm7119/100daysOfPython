a=True
b=False
c=True


if a and b:
    print("both are true")
else:
    print("one or both are false")

if a or c:
    print("at least one is true")

print(f"not \"a:{a}\" is", not a)