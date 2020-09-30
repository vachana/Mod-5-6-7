def filter_evens(number_list):
    ''' function: returns list of the evens of list
        parameters: list
        returns: list of the even values'''
    list_of_evens = []
    for i in range(7):
        if number_list[i] % 2 == 0:
            list_of_evens.append(number_list[i])
    return list_of_evens

def main():
    list_of_numbers = [-2, 4, 17, 2006, 2, 5, 8]

    print(filter_evens(list_of_numbers))



main()
        
