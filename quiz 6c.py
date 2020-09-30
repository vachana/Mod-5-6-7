def add_spaces(user_list):
    user_list = []
    index = 0
    spaced_word = " "
    while (index < len(user_list)):
        spaced_word += user_list[index] + "   " + "\n"
    index += 1
    return spaced_word



#how to get to print on same line
        

def main():

    list_input = ["Hey", "Howdy", "hiya"]
    

    print(add_spaces(list_input))



main()
