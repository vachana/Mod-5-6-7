def compare_lists(list_one, list_two):
    ''' function: compares two lists and returns true if order and numbers are the same
        parameters: two lists
        returns: true or false'''
    
    for i in range(8):
        if (list_one[i] == list_two[i]) and (len(list_one) == len(list_two)):
            result = "True"
        else:
            result = "False"
            

    return result

def main():

    list_one = [2, 4, 6, 8, 10, 12, 16, 16]
    list_two = [3, 4, 6, 8, 10, 13, 16, 17]

    print(compare_lists(list_one, list_two))




main()
