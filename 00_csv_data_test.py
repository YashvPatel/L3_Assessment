import random

some_animal = [
     ['Aardvark', 'cub'],
     ['Albatross', 'chick'],
     ['Alligator', 'hatchling'],
     ['Alpaca', 'cria'], ['Anteater', 'pup'],
     ['Antelope', 'calf']
]

current_output = random.choice(some_animal)

for item in some_animal:
    print(item[0])
    # print(item)
