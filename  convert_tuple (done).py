def convert_tuple(tuple_input):
    ''' function: takes tuple and converts to list
        parameters: one tuple
        returns: same tuple but as a list'''
    index = 0
    list_form = []
    while len(list_form) < len(tuple_input):
        list_form.append(tuple_input[index])
        index += 1

    return list_form
        

def main():
    tuple_input = ("My", "Name" , "Is", "Katie")
    print(convert_tuple(tuple_input))
    
    

main()

    
