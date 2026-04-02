from validators import stations, get_station, get_passenger_type
from fare_calculator import calculate_zones, calculate_fare, display_ticket


def main():

    print("=================================")
    print("Centrala Transport Authority")
    print("Underground Ticketing System")
    print("=================================")

    while True:

        passenger_type = get_passenger_type()

        origin = get_station("Enter departure station: ")
        destination = get_station("Enter destination station: ")

        origin_zone = stations[origin]
        destination_zone = stations[destination]

        zones = calculate_zones(origin_zone, destination_zone)

        fare = calculate_fare(origin_zone, destination_zone, passenger_type)

        display_ticket(origin, destination, zones, passenger_type, fare)

        again = input("\nDo you want another ticket? (y/n): ")

        if again.lower() != "y":
            print("Thank you for using CTA ticket system")
            break


if __name__ == "__main__":
    main()
