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

    station_list = list(stations.keys())

    while True:

        print("\nAvailable Stations:")
        for i, station in enumerate(station_list, 1):
            print(f"{i}. {station}")

        try:
            choice = int(input(message))

            if 1 <= choice <= len(station_list):
                return station_list[choice - 1]
            else:
                print("Invalid number. Please choose a valid station.")

        except ValueError:
            print("Please enter a number.")


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
