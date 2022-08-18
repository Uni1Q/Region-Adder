import csv
import sys
import easygui
import os

# generates a list to be populated with selected csv files
country_data = []
user_data = []


# reads reference data
def reference_read():

    # default path
    path = "region_data.csv"

    while True:
        try:
            with open(path) as data:
                reader = csv.reader(data)
                for item in reader:
                    country_data.append(item)
        except FileNotFoundError:
            # if file not found opens box to let user enter their own path
            directory = os.getcwd()
            print(f"File not found in {directory}\{path}, please input new file location")
            path = easygui.fileopenbox(msg="Please enter file location ", default='*', filetypes=["*.csv"])
            if check_file_type(path):
                break
            else:
                print(f"Unsupported filetype \n")
        else:
            break


# reads user data
def data_read():

    while True:
        path = easygui.fileopenbox(msg="Please enter file location ", default='*', filetypes=["*.csv"])
        if check_file_type(path):
            break
        else:
            print("Unsupported filetype.\n")

    while True:
        try:
            with open(path) as data:
                reader = csv.reader(data)
                for item in reader:
                    user_data.append(item)
        except FileNotFoundError:
            directory = os.getcwd()
            print(f"File not found in {directory}/{path}, please input new file location")
            path = easygui.fileopenbox(msg="Please enter valid file location ", default='*', filetypes=["*.csv"])
        else:
            break


# main
def run():
    print("Opening reference data\n")
    reference_read()
    print("Reference data success\n\n")
    print("Opening user data")
    data_read()
    length = data_length(user_data)

    print(f"There are {length-1} items in the data set")
    print("User data success\n\n")
    print("What format are the countries in your .csv file?\n")
    print("Full name        (Brazil)            [1]")
    print("Alpha-2          (PL)                [2]")
    print("Alpha-3          (LTU)               [3]")
    print("Country Code     (050)               [4]")
    print("ISO-3166-2       (ISO 3166-2:BE)     [5]")

    while True:
        try:
            country_format = int((input("User Input: ")))
            if country_format not in {1, 2, 3, 4, 5}:
                print("Wrong input")
        except ValueError:
            print("Wrong value")
        else:
            break

    print("Please enter the index of the country in your csv file")
    while True:
        try:
            country_index_location = int(input("User input: "))
        except ValueError:
            print("Please enter valid index")
        else:
            country_exists, total_matching = check_country_existence(country_index_location, country_format)
            if country_exists:
                print(f"\nSuccessfully matched {total_matching} countries out of {data_length(user_data)-1} items in the data set\n\n")
                break
            else:
                sys.exit("\nNo matching countries found for given index.")

    print("What would you like to add to your data set?\n")
    print("Note - Items will be added in the order selected\n")
    print("Full name            (Portugal)          [1]")
    print("Alpha-2              (AT)                [2]")
    print("Alpha-3              (BGR)               [3]")
    print("Country Code         (208)               [4]")
    print("ISO-3166-2           (ISO 3166-2:DO)     [5]")
    print("Region               (Oceania)           [6]")
    print("Sub-Region           (South America)     [7]")
    print("Intermediate-region  (Caribbean)         [8]")
    print("Region Code          (009)               [9]")
    print("Sub-Region Code      (154)               [10]")
    print("Quit             (Quit)              [0]\n")

    added_details = []
    while True:
        try:
            user_choice = int(input("User Input: "))
            if user_choice == 0:
                break
            elif user_choice in range(1, 11):
                if user_choice-1 in added_details:
                    print("Item is already in the list")
                else:
                    added_details.append(user_choice-1)
            else:
                print("Invalid Input")

        except ValueError:
            print("Wrong value")

    print("\nGenerating new csv file\n")
    region_adder(added_details, country_index_location, country_format)

    print("\nOperation complete! Thanks for using my program")


# Makes a new csv file containing old data and selected new data
def region_adder(added_details, country_index_location, country_format):

    header = generate_header(added_details)
    fail_count = 0

    # adds the data to the new csv file
    with open("new_data.csv", "w", newline="") as write_file:
        writer = csv.writer(write_file)
        writer.writerow(header)

        # generates a new line with selected options
        for i in range(1, data_length(user_data)):
            new_row, found_data = generate_row(i, added_details, country_index_location, country_format)
            if not found_data:
                print(f"No matching country found in line {i}, country name in user data {user_data[i][country_index_location]}")
                fail_count += 1
            writer.writerow(new_row)

    if fail_count > 0:
        print(f"{fail_count} countries couldn't be completed")


def generate_row(row, added_details, country_index_location, country_format):

    current_row = user_data[row]

    # finds the matching country in the list and generates a new row with selected user details
    for i in range(1, data_length(country_data)):
        if country_data[i][country_format-1].upper() == user_data[row][country_index_location].upper():
            # print(country_data[i][country_format - 1], end="")
            # print(user_data[row][country_index_location], end="")
            # print(" Success! ", end="")
            new_row = current_row
            for item in added_details:
                new_row.append(country_data[i][item])
            return new_row, True

    return current_row, False


# generates a header
def generate_header(added_details):

    header = user_data[0]

    for item in added_details:
        header.append(country_data[0][item])

    return header


# Checks if countries exist for given index
def check_country_existence(country_index_location, country_format):
    total_matching_countries = 0
    for i in range(1, data_length(country_data)):
        for j in range(1, data_length(user_data)):
            if country_data[i][country_format-1].upper() == user_data[j][country_index_location].upper():
                total_matching_countries += 1
    if total_matching_countries > 0:
        return True, total_matching_countries
    else:
        return False, total_matching_countries


def check_file_type(path):
    try:
        user_file = path.split(".")
        if user_file[-1] == "csv":
            return True
    except AttributeError:
        sys.exit("Quit Successfully")
    else:
        return False


# Obtains length of provided data
def data_length(data):

    length = len(data)
    return length


if __name__ == "__main__":
    run()
