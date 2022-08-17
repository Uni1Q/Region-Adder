import csv
import easygui
import os

region_data = []
change_data = []


def reference_read():
    path = "region_data.csv"

    while True:
        try:
            with open(path) as data:
                reader = csv.reader(data)
                for item in reader:
                    region_data.append(item)
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
            print(f"File not found in {directory}\{path}, please input new file location")
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
    print("Change data success")


if __name__ == "__main__":
    run()
