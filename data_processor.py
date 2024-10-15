while True:
    first = input("What is your first name?")
    if len(first) < 2:
        print("Your name must be at least 2 characters long.")
    else:
        break

while True:
    last = input("What is your first name?")
    if len(last) < 2:
        print("Your name must be at least 2 characters long.")
    else:
        break

print(f"Hello {first} {last}.")