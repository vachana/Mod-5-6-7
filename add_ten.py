def add_ten(list_of_numbers):
    '''function: adds ten to each integer in list
        parameters: list of integers
        returns: list with 10 added to each integer'''
    new_list = []
    for i in range (5):
        new_value = list_of_numbers[i] + 10
        new_list.append(new_value)

    return new_list


def main():
    numbers = [6, 12, 4, 60, -10]

    print(add_ten(numbers))


main()
        

    
