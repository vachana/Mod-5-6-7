def to_numbers(user_list):
    '''function: receives list of string values and returns list of floats
        parameters: list of string vlaues
        returns: list of floats'''

    i = 0
    new_list = []
    while i < len(user_list):
        new_float = float(user_list[i])
        new_list.append(new_float)
        i += 1
    return new_list



def main():

    list_of_strings = ["7", "20005", "200.86", "-64"]

    list_of_floats = to_numbers(list_of_strings)
    print(type(list_of_floats))
    print(list_of_floats)
    print(type(list_of_floats[2]))


main()

