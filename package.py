# This creates the Package class.

import hashmap
import csv


class Package:
    def __init__(self, package_id, address, deadline, city, zip_code, weight):
        self.package_id = package_id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zip_code = zip_code
        self.weight = weight
        self.hub_departure_time = None
        self.delivery_status = None
        self.delivery_time = None

    def __str__(self):
        return 'Package ID: %s \tAddress: %-20s \tDeadline: %-5s \tCity: %-15s \tZIP: %s \tWeight: %s kg \tDelivery Status: %-10s \tDelivery Time: %s' % (
        self.package_id, self.address, self.deadline, self.city, self.zip_code, self.weight, self.delivery_status,
        self.delivery_time)

    # Updates the delivery status to "at the hub", "en route", or "delivered".
    def update_delivery_status(self, user_selected_time):
        # Checks if the hub departure time is greater than (occurs after) the user selected time.
        if self.hub_departure_time > user_selected_time:
            self.delivery_status = "at the hub"
            self.delivery_time = None

        # Check if the delivery time is greater than (occurs after) the user selected time.
        elif self.delivery_time > user_selected_time:
            self.delivery_status = "en route"
            self.delivery_time = None

        else:
            # Updates delivery_status to "delivered" if the package's hub departure occured before the user selected time and if the package's delivery time occured before the selected time.
            self.delivery_status = "delivered"


# Loads data from the csv file into the packages hash table.
def loadPackageData(fileName):
    with open(fileName) as packages:
        packageData = csv.reader(packages)
        for row in packageData:
            package_id = int(row[0])
            address = row[1]
            deadline = row[5]
            city = row[2]
            zip_code = int(row[4])
            weight = int(row[6])
            package_info = Package(package_id, address, deadline, city, zip_code, weight)
            packageHash.insert(package_id, package_info)


# Creates a chained hash table for packages.
packageHash = hashmap.HashTable()
# Loads data from the WGUPSPackageFile.csv into the packages hash table.
loadPackageData('CSV/WGUPSPackageFile.csv')
