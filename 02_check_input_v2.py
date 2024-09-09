def check_quiz(min_value):
    error = "Enter a number that is more than 1 & less than 100" \
            .format(min_value)

    try:
        response = int(input("Choose a number: "))

        if response < 1 or response > 100:
            print(error)
        else:
            return response

    except ValueError:
        print(error)


# *** Main routine ****

while True:
    to_check = check_quiz(1-100)
