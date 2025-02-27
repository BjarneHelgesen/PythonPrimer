def input_int(prompt):
    while True:
        try:
            int_value =  int(input(prompt))
            break
        except ValueError:
            ...
    return int_value

age = input_int("What is your age:")

