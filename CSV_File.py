import csv


def get_all_data(self):
    with open("animals_young_collective.csv", "r") as file:
        var_all_data = list(csv.reader(file, delimiter=","))
        # Remove the header row from the data.
        var_all_data.pop(0)
