def calculate_zones(origin_zone, destination_zone):
    zones = abs(origin_zone - destination_zone) + 1
    return zones


def calculate_fare(origin_zone, destination_zone, passenger_type):

    price_per_zone = 2

    zones = calculate_zones(origin_zone, destination_zone)

    fare = zones * price_per_zone

    if passenger_type == "Student":
        fare = fare * 0.5

    elif passenger_type == "Senior":
        fare = fare * 0.7

    return round(fare, 2)


def display_ticket(origin, destination, zones, passenger_type, fare):

    print("\n------ CTA Underground Ticket ------")
    print("From:", origin)
    print("To:", destination)
    print("Zones Travelled:", zones)
    print("Passenger Type:", passenger_type)
    print("Ticket Price: $", fare)
