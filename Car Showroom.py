
cars = []

while True:
    print("\n--- Car Showroom ---")
    print("1. Add Car")
    print("2. Show Cars")
    print("3. Search Car")
    print("4. Sell Car")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter car name: ")
        price = input("Enter car price: ")
        cars.append([name, price])
        print("Car added successfully!")

    elif choice == "2":
        for car in cars:
            print("Name:", car[0], "| Price:", car[1])

    elif choice == "3":
        name = input("Enter car name: ")
        for car in cars:
            if car[0] == name:
                print("Car found:", car)
                break
        else:
            print("Car not found!")

    elif choice == "4":
        name = input("Enter car name: ")
        for car in cars:
            if car[0] == name:
                cars.remove(car)
                print("Car sold successfully!")
                break
        else:
            print("Car not found!")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
