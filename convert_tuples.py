def convert_tuple(user_tuple):
    '''function: takes tuple input and returns a list that contains same elements and order
        parameters: one tuple
        return: list with same elements and order as tuple'''

    new_list = []
    i = 0
    while i < len(user_tuple):
        new_list.append(user_tuple[i])
        i += 1

    return new_list

def main():

    user_tuple = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

    tuple_as_list = convert_tuple(user_tuple)
    print(tuple_as_list)
    print(type(tuple_as_list))

main()
                    
