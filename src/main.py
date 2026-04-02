#!/usr/bin/env python3

from fare_calculator import calculate_fare, display_fare
from validators import get_zone_input


def main():
    print("=" * 40)
    print("CTA Ticketing System")
    print("Zone Fare Calculator")
    print("=" * 40)

    while True:
        print("\n--- New Ticket Calculation ---")

        origin = get_zone_input("Enter departure zone: ")
        destination = get_zone_input("Enter destination zone: ")

        fare = calculate_fare(origin, destination)

        display_fare(origin, destination, fare)

        choice = input("\nDo you want to calculate another fare? (y/n): ")

        if choice.lower() != 'y':
            print("Thank you for using the system.")
            break


if __name__ == "__main__":
    main()
