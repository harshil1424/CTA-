def calculate_fare(origin, destination):
    base_fare = 2
    zone_difference = abs(origin - destination)

    fare = base_fare + zone_difference

    return fare


def display_fare(origin, destination, fare):
    print("\n----- Ticket Details -----")
    print("Origin Zone:", origin)
    print("Destination Zone:", destination)
    print("Ticket Fare: $", fare)
