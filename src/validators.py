def get_zone_input(message):
    while True:
        try:
            zone = int(input(message))

            if zone < 1 or zone > 5:
                print("Please enter a zone between 1 and 5.")
            else:
                return zone

        except ValueError:
            print("Invalid input. Please enter a number.")
