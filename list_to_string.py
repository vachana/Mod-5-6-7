def list_to_string(list_input):
    '''function: takes a list and returns a string with each on own line
        parameters: list
        returns: string on own line'''
    new_line = " "
    index = 0
    while index < len(list_input):
        new_line = list_input[index] + "\n" + new_line
        index += 1
    return new_line

#why an empty string?!

def main():
    
    list_input = ["hello", "my", "name", "is", "Katie"]
    print(list_to_string(list_input))
     
    



main()
