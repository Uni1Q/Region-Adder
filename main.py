import csv
import sys
import easygui
import os

#generates a list to be populated with selected csv files
country_data = []
user_data = []


def reference_read():
    path = "region_data.csv"

    while True:
        try:
            with open(path) as data:
                reader = csv.reader(data)
                for item in reader:
                    country_data.append(item)
        except FileNotFoundError:
            directory = os.getcwd()
            print(f"File not found in {directory}\{path}, please input new file location")
            path = easygui.fileopenbox(msg="Please enter valid file location ", default='*', filetypes=["*.csv"])
        else:
            break


def data_read():

    path = "C:/Users/rokas/Desktop/ds_salaries.csv"

    # path = easygui.fileopenbox(msg="Please enter file location ", default='*', filetypes=["*.csv"])

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


def run():
    print("Opening reference data")
    reference_read()
    print("Reference data success\n\n")
    print("Opening change data")
    data_read()
    length = data_length(user_data)

    print(f"There are {length-1} items in the data set")
    print("Change data success\n\n")
    print("What format are the countries in your .csv file?")
    print("Full name (Brazil) [1]")
    print("Alpha-2 (PL) [2]")
    print("Alpha-3 (LTU) [3]")
    print("Country Code (050) [4]")
    print("ISO-3166-2 (ISO 3166-2:BE) [5]")

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
                print(f"Successfully matched {total_matching} countries out of {data_length(user_data)-1} items in the data set\n\n")
                break
            else:
                sys.exit("No matching countries found for given index.")

    print("What would you like to add to your data set?\n")
    print("Note - Items will be added in the order selected\n")
    print("Full name        (Portugal)          [1]")
    print("Alpha-2          (AT)                [2]")
    print("Alpha-3          (BGR)               [3]")
    print("Country Code     (208)               [4]")
    print("ISO-3166-2       (ISO 3166-2:DO)     [5]")
    print("Region           (Oceania)           [6]")
    print("Sub-Region       (South America)     [7]")
    print("Region Code      (009)               [8]")
    print("Sub-Region Code  (154)               [9]")
    print("Quit             (Quit)              [0]\n")

    added_details = []
    while True:
        try:
            user_choice = int(input("User Input: "))
            if user_choice == 0:
                break
            elif user_choice in range(1, 10):
                if user_choice in added_details:
                    print("Item is already in the list")
                else:
                    added_details.append(user_choice)
            else:
                print("Invalid Input")

        except ValueError:
            print("Wrong value")

    region_adder()


def region_adder():
    pass


def check_country_existence(country_index_location, country_format):
    total_matching_countries = 0
    for i in range(1, data_length(country_data)):
        for j in range(1, data_length(user_data)):
            if country_data[i][country_format-1] == user_data[j][country_index_location]:
                total_matching_countries += 1
    if total_matching_countries > 0:
        return True, total_matching_countries
    else:
        return False, total_matching_countries


def data_length(data):

    length = len(data)
    return length


if __name__ == "__main__":
    run()
