stations = {
    "Centrala": 1,
    "Jaund": 1,
    "Soth": 1,
    "Norvia": 2,
    "Eston": 2,
    "Zord": 3,
    "Velka": 3
}


def get_station(message):

    while True:

        print("\nAvailable Stations:")
        for station in stations:
            print("-", station)

        name = input(message)

        if name in stations:
            return name
        else:
            print("Station not found. Please enter a valid station name.")


def get_passenger_type():

    print("\nPassenger Type")
    print("1. Adult")
    print("2. Student")
    print("3. Senior")

    while True:

        choice = input("Enter choice: ")

        if choice == "1":
            return "Adult"

        elif choice == "2":
            return "Student"

        elif choice == "3":
            return "Senior"

        else:
            print("Invalid choice")
