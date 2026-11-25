
cars = ["BMW", "Mercedes", "Toyota", "Audi", "Porsche"]
reservations = []

while True:
    print("\n--- Car Reservation System ---")
    print("1. Show Cars")
    print("2. Reserve Car")
    print("3. Show Reservations")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("\nAvailable Cars:")
        for car in cars:
            print(car)

    elif choice == "2":
        car = input("Enter car name: ")

        if car in cars:
            reservations.append(car)
            cars.remove(car)
            print("Car reserved successfully!")
        else:
            print("Car not available!")

    elif choice == "3":
        print("\nYour Reservations:")
        for car in reservations:
            print(car)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
