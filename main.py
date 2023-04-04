from package import *
from truck import *
import distances
import datetime


# This asks the user if they would like to exit the program. A Boolean is returned. True to continue the program or False to exit the program.
def exit_prompt():
    valid_input = False
    # The user must enter Y or N to exit the while not loop.
    while not valid_input:
        user_input = input("\nWould you like to exit the program? Please type Y for YES and N for NO: ")
        if user_input.lower() == "y":
            # Returns false, thus exiting the program.
            return False
        elif user_input.lower() == "n":
            # Return true, thus continuing the program.
            return True
        else:
            print("Invalid input. Please enter Y or N.")
            # the while not loop continues until user enters either Y or N.
            valid_input = False


# This takes a user input for time and returns it as datatime.timedelta
def select_time_prompt():
    valid_input = False
    # The user must enter a time in the valid format of HH:MM:SS.
    while not valid_input:
        user_input = input("Please enter a time (format HH:MM:SS): ")
        # Splits user_input into three parts to extract hours, minutes, and seconds.
        time_parts = user_input.split(':')
        if len(time_parts) != 3:
            # Displays when a user input did not have two colons to split the user_input into three parts.
            print("Invalid input format. Please enter time in HH:MM:SS format.")
        else:
            try:
                # Assigns the three split parts into the three variables: hours, minutes, seconds
                hours, minutes, seconds = map(int, time_parts)
                user_selected_time = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
                # Exits the while not loop and returns the user selected time.
                valid_input = True
                return user_selected_time
            except ValueError:
                # Displays when the user did not enter a valid time.
                print("Invalid input format. Please enter time in HH:MM:SS format.")


# Prints to console
print("WGUPS ROUTING PROGRAM")
print("---------------------------------------------------")
print("Welcome! This program allows for you to view details about packages or trucks at WGUPS.")

# The program will continue to run and not exit until a user input changes continue_program to False.
continue_program = True
while continue_program:
    # The user has an option of viewing information about packages or trucks by entering 1 or 2.
    print("\nPlease type a number listed below to make a selection:")
    print("1.\tPackages \n2.\tTrucks")
    user_input = input()

    # Checks if user entered 1 for Packages
    if user_input == "1":
        print("PACKAGES selected")
        # select_time_prompt() is called and assigned to user_selected_time as datatime.timedelta
        user_selected_time = select_time_prompt()
        user_input = input(
            "Please enter package ID to view a package's info or type ALL to view the information of all packages: ")
        # Checks if user entered "ALL" to view information for all packages.
        if user_input.lower() == "all":
            # Loops through packages with id 1 through 40.
            for packageID in range(1, 41):
                # The package from the hash is assigned to the variable package
                package = packageHash.search(packageID)
                # The package's delivery status is then updated accordingly depending on the time the user entered.
                package.update_delivery_status(user_selected_time)
                # Prints the newly updated package information to the console.
                print(package)
            # The total mileage for truck1, truck2, and truck3 is calculated and assigned to total_mileage.
            total_mileage = truck1.mileage + truck2.mileage + truck3.mileage
            # Prints total_mileage to console.
            print("-----------------------------------------------------------------")
            print("Total mileage for all trucks to make all deliveries: %.1f miles" % total_mileage)

        # Checks if user entered a digit.
        elif user_input.isdigit():
            try:
                # User input is assigned to the variable package_id
                package_id = int(user_input)
                # Searches for the package id in the chained hash table and assigns it to package.
                package = packageHash.search(package_id)
                # The package's delivery status is then updated accordingly depending on the time the user entered.
                package.update_delivery_status(user_selected_time)
                # Prints the newly updated package information to the console.
                print(package)
            except AttributeError:
                # Displays when user entered a package id that does not exist in the chained hash table.
                print("Invalid input. No package with the id %s was found." % user_input)
        else:
            # Displays when user did not enter ALL or a digit.
            print("Invalid input.")

        # exit_prompt() is initiated. The boolean returned determines whether the program will continue to run (True) or exit (False).        continue_program = exit_prompt()
        continue_program = exit_prompt()

    # Checks if user entered 2 for Trucks
    elif user_input == "2":
        print("TRUCKS selected")
        # Information for the truck instances are printed
        print(truck1)
        print(truck2)
        print(truck3)
        # The total mileage for truck1, truck2, and truck3 is calculated and assigned to total_mileage.
        total_mileage = truck1.mileage + truck2.mileage + truck3.mileage
        # Prints total_mileage to console.
        print("__________________________________________")
        print("Total mileage for all trucks: %.1f miles" % total_mileage)

        # exit_prompt() is initiated. The boolean returned determines whether the program will continue to run (True) or exit (False).
        continue_program = exit_prompt()

    # If user entered anything other than 1 or 2, a message is displayed to console.
    else:
        print("Invalid entry")
        # exit_prompt() is initiated. The boolean returned determines whether the program will continue to run (True) or exit (False).
        continue_program = exit_prompt()
