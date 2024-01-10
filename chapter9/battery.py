class Battery:
    """ A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=40):
        """ Initialize the battery attributes """
        self.battery_size = battery_size
        # self.range = 0

    def describe_battery(self):
        """ Print the statement describing battery size """
        print(f"This car has a battery of {self.battery_size}-kWh")

    def get_range(self):
        """ Print the statement describing battery range """
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car has a range of {range} on full charge")
