def read_values(input_number):
    ''' function: prints a positive list of inputted integers
        parameters: positive integers
        return: integers in list'''

    new_list = []

    while (input_number > 0):
        new_list.append(input_number)
        input_number = int(input("Please enter a number: "))
           
    return new_list

def main():

    input_number = int(input("Please enter a number: "))
    print(read_values(input_number))
    
    

main()
            

                       
