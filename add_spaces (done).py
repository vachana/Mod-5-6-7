def add_spaces(word):
    index = 0
    spaced_word = " "
    while (index < len(word)):
        spaced_word += word[index] + "   "
        index += 1
    return spaced_word


#how to get to print on same line
        

def main():
    
    user_input = input("Please enter your word:\n ")

    print(add_spaces(user_input))



main()
           
