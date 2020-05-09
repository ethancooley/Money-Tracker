def process_file(filename):
    try:
        # Make list of all values in file
        f = open(filename, "r")
        regular = f.readlines()
        f.close()
    except FileNotFoundError:
        raise ValueError('Error: String does not represent a valid file!')
    except IndexError:
        print('Error: Not enough command line arguments!')
        quit()
    # Move all items into lists and change from strings to floats
    income_list = [float(regular[0]), float(regular[2]), float(regular[4]), float(regular[6]), float(regular[8]),
                   float(regular[10]), float(regular[12])]
    expense_list = [float(regular[1]), float(regular[3]), float(regular[5]), float(regular[7]), float(regular[9]),
                    float(regular[11]), float(regular[13])]

    # Return tuple containing both lists
    both_lists = (income_list, expense_list)
    return both_lists