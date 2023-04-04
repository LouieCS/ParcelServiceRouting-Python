# This creates the Parcel Truck class.

import datetime


class ParcelTruck:
    # Variable assign an id number to the truck
    next_truck_id = 1

    def __init__(self, packages, hub_departure_time=None, max_capacity=16, speed=18, mileage=0,
                 current_location="4001 South 700 East"):
        # Checks to ensure the number of packages in the truck does not exceed the maximum capacity.
        if len(packages) > max_capacity:
            raise ValueError("Number of packages exceeds the truck's maximum capacity.")
        # Assigns a number to the truck and increments the next_id counter
        self.truck_id = ParcelTruck.next_truck_id
        ParcelTruck.next_truck_id += 1

        self.max_capacity = max_capacity
        self.packages = packages
        self.hub_departure_time = hub_departure_time
        self.speed = speed
        self.mileage = mileage
        self.current_location = current_location
        self.time = hub_departure_time

    def __str__(self):
        return "Truck #%-3s Max. Capacity: %-4s Packages: %-65s Hub Departure: %-8s Speed: %-3s Mileage: %-5s Current Location: %s" % (
        self.truck_id, self.max_capacity, self.packages, self.hub_departure_time, self.speed, round(self.mileage, 1),
        self.current_location)


# Instances of ParcelTruck with a list of packages assigned and time for hub departure.
truck1 = ParcelTruck([1, 13, 14, 15, 19, 16, 20, 21, 34, 4, 40, 39, 10, 30, 37, 29], datetime.timedelta(hours=8, minutes=0))
truck2 = ParcelTruck([3, 18, 36, 38, 6, 25, 28, 32, 5, 31, 7], datetime.timedelta(hours=9, minutes=10))
# An instance of ParcelTruck with a list of packages assigned.
truck3 = ParcelTruck([9, 8, 27, 35, 2, 33, 24, 26, 11, 23, 17, 12, 22])
