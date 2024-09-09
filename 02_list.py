import random

some_choices = [
    ['Aardvark', 'cub'],
    ['Albatross', 'chick'],
    ['Alligator', 'Hatchling'],
    ['Alpaca', 'cria'],
    ['Anteater', 'pup']
]

for item in some_choices:
    print(item[0])


my_choice = random.choice(some_choices)
print(my_choice)

question = my_choice[0]
answer = my_choice[1]

print(f"Question: {question} | Answer: {answer}")
