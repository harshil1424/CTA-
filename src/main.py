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
    1  print("Welcome to CTA Ticketing System")

2  # Passenger type selection
3  print("Choose Passenger Type:")
4  print("1. Adult")
5  print("2. Senior")
6  print("3. Student")

7  passenger_choice = int(input("Enter your choice (1-3): "))

8  if passenger_choice == 1:
9      passenger_type = "Adult"
10     fare = 5
11 elif passenger_choice == 2:
12     passenger_type = "Senior"
13     fare = 3
14 elif passenger_choice == 3:
15     passenger_type = "Student"
16     fare = 2
17 else:
18     print("Invalid choice")
19     exit()

20 print("Passenger Type:", passenger_type)
21 print("Ticket Price:", fare)
