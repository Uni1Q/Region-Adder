import csv
import easygui
import os

#generates a list to be populated with selected csv files
country_data = []
change_data = []


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
                    change_data.append(item)
        except FileNotFoundError:
            directory = os.getcwd()
            print(f"File not found in {directory}/{path}, please input new file location")
            path = easygui.fileopenbox(msg="Please enter valid file location ", default='*', filetypes=["*.csv"])
        else:
            break


def run():
    print("Opening reference data")
    reference_read()
    print("Reference data success")
    print(" ")
    print("Opening change data")
    data_read()
    length = data_length(change_data)
    print(f"There are {length-1} items in the data set")
    print("Change data success\n\n")

    while True:

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

        while True:
            try:
                country_index_location = int(input("Please enter the index of the country in your csv file: "))
                if check_country_existence(country_index_location, country_format):
                    continue
                else:
                    print("No matching countries found for given index.")

            except ValueError:
                print("Please enter valid index")
            else:
                break


def check_country_existence(country_index_location, country_format):

    for i in range(data_length(country_data)):
        for j in range(data_length(change_data)):
            if country_data[country_format-1][i] == change_data[country_index_location][j]:
                return True


def data_length(data):

    length = len(data)
    return length


if __name__ == "__main__":
    run()
