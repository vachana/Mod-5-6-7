def positional_elements(user_list):
    ''' function: calculates how many element arguments equal the index of the element
        parameters: one list
        returns: number of elements that match the index value'''

    new_list = []

    for i in range(len(user_list)):
        if user_list[i] == i:
            new_list.append(user_list[i])
            
    number_of_matches = len(new_list)

    return number_of_matches


def main():

    user_list = [0, 3, 1, 4, 4, 17]

    print(positional_elements(user_list))



main()
