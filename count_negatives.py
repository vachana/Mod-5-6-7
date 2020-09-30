def count_negatives(list_of_numbers):
    '''function: counts how many negative numbers in a list
        parameters: one list
        returns: how many negatives in the list'''
    
    negatives_list = []
    i = 0
    
    while i < len(list_of_numbers):
        if list_of_numbers[i] < 0:
            negatives_list.append(list_of_numbers[i])
        i += 1
        

    return len(negatives_list)


def main():

    lst_of_numbers = [-16, 20, 1.0, -3.4, -16, 9, -16]

    print(count_negatives(lst_of_numbers))


main()
            
