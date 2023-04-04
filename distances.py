# This creates the nearest neighbor algorithm used to arrange the order of the packages for delivery.

from package import *
from truck import *
import csv

with open("CSV/WGUPSDistanceTable.csv") as addresses:
    addressData = csv.reader(addresses)

    # Creates an empty list for hubs.
    list_addresses_data = []

    # Adds the first three columns, which contains address information, to the list if the first column is not empty.
    for row in addressData:
        if row[0]:
            list_addresses_data.append([int(row[0]), row[1], row[2]])

with open("CSV/WGUPSDistanceTable.csv") as distances:
    distanceData = csv.reader(distances)

    # Creates an empty list for distances.
    list_distances_data = []

    # Adds columns indexed 3 to 29, which contains distance information, to the list if the first column is not empty.
    for row in distanceData:
        if row[0]:
            csv_distance_columns = []
            for i in range(3, 30):
                if row[i]:
                    csv_distance_columns.append(float(row[i]))
                else:
                    csv_distance_columns.append(row[i])
            list_distances_data.append(csv_distance_columns)


# Returns the index of the address matching in the list_address_data list.
def address_index(address):
    for row in list_addresses_data:
        if address in row[2]:
            return int(row[0])


# Retrieves the distance between two addresses.
def distance(address_one, address_two):
    distance = list_distances_data[address_one][address_two]
    if distance == '':
        distance = list_distances_data[address_two][address_one]
    return float(distance)


# Arranges the order of the packages for delivery based on nearest neighbor.
def delivery_route(truck):
    # An empty list for the undelivered queue.
    undelivered_packages_queue = []
    # Iterates through the package hash table and inserts one package into an undelivered queue one at a time.
    for packageID in truck.packages:
        # A package from the hash is assigned to the variable package.
        package = packageHash.search(packageID)
        # The package's hub departure time is updated to match the assigned truck's departure time.
        package.hub_departure_time = truck.hub_departure_time
        # Package is added to the queue.
        undelivered_packages_queue.append(package)

    # Removes the truck's packages for rearrangement.
    truck.packages.clear()

    # One package is removed from undelivered_packages_queue each iteration and added to the truck.
    while len(undelivered_packages_queue) > 0:
        # The first package in the list is assigned as a temporary placeholder for the variable next_package.
        next_package = undelivered_packages_queue[0]
        # The distance between the the truck's current location and the next_package's location is calculated and assigned to nearest_address_distance.
        nearest_address_distance = distance(address_index(truck.current_location), address_index(next_package.address))
        # Iterates through the undelivered packages list.
        for package in undelivered_packages_queue:
            # Compares to see if there exists a package in the undelivered queue that has a shorter distance from the truck's location than the value assigned to nearest_address_distance.
            if distance(address_index(truck.current_location), address_index(package.address)) <= nearest_address_distance:
                # The new shorter distance to the package from the truck's location is assigned to the variable.
                nearest_address_distance = distance(address_index(truck.current_location), address_index(package.address))
                # The package is assigned as the next package to be delivered.
                next_package = package

        # Removes the package from the undelivered_packages_queue list
        undelivered_packages_queue.remove(next_package)
        # Adds the package to truck.
        truck.packages.append(next_package.package_id)
        # Calculates the distance the truck travels for the delivery.
        truck.mileage += nearest_address_distance
        # Updates the truck's current location as the package's destination's address.
        truck.current_location = next_package.address
        # Updates the time after calculating the time it took for delivery.
        truck.time += datetime.timedelta(hours=nearest_address_distance / truck.speed)
        # Assigns the delivery time from the truck's time after delivery
        next_package.delivery_time = truck.time
        # Assigns the time which the package departed from the hub with the truck.
        next_package.departure_time = truck.hub_departure_time

    # Calculates & updates the time it took for return to hub after delivering all packages assigned to the truck.
    return_to_hub_distance = distance(address_index(truck.current_location), 0)
    truck.mileage += return_to_hub_distance
    truck.current_location = "4001 South 700 East"
    truck.time += datetime.timedelta(hours=return_to_hub_distance / truck.speed)


# Arranges the order of the truck's packages for delivery based on next nearest address / neighbor.
delivery_route(truck1)
delivery_route(truck2)

# truck3's departure time is updated to when either truck1 or truck2 returns to the hub after completing all deliveries.
truck3.hub_departure_time = min(truck1.time, truck2.time)
truck3.time = truck3.hub_departure_time
# Arranges the order of the truck's packages for delivery based on next nearest neighbor.
delivery_route(truck3)
