def name_number(user_name):
    '''function: sums up the letters of the name to return a numeric value
        parameters: one string
        returns: sum of letters turned into numbers'''
    i = 0
    list_of_letters = []
    while i < len(user_name):
        letter_number = ord(user_name[i]) - 96
        i += 1
        list_of_letters.append(letter_number)

    return sum(list_of_letters)

def main():
    user_name =input("Enter Your Name: \n")
    print(name_number(user_name.lower())) 


main()
