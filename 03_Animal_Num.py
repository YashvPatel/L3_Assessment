import csv

file = open("animals_young_collective.csv", "r")
all_animals = list(csv.reader(file, delimiter=","))
file.close()

# remove the first row (header values)
all_animals.pop(0)

# get the first 50 rows (used to develop animal
# buttons for play GUI)
print(all_animals[:50])

print("Length: {}".format(len(all_animals)))
