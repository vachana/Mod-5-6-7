#come back and watch video again on creating a menu in mod 5
    
def menu():   
    quit_option = "0. Quit"
    option_one = '1. Add "0"'
    option_two = '2. Add "oo"'
    option_three = '3. Add "xXx"'

    
    

        
def main():
    #program prints the menue screen and reads in the options selected
    
    str_menu = []
    quit_option = "0. Quit"
    option_one = '1. Add "0"'
    option_two = '2. Add "oo"'
    option_three = '3. Add "xXx"'
    
    string_one = "0"
    string_two = "oo"
    string_three = "xXx"

    print(menu())

    user_input = input("Please select from the menu")
    
    

    while (user_option != 0):
        print(menu())
        user_input = input("Please select from the menu")
        
        
        if (user_input != 0) or (user_input != 1) or (user_input != 2) or (user_input !=3):
            print("Invalid Response")
        if user_input == 1:
            str_menu.append(string_one)
        elif user_input == 2:
            str_menu.append(string_two)
        elif user_input == 3:
            str_menu.append(string_three)
        elif user_input == 0:
            break

    print(str_menu())
        


main()
