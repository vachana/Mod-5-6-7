# program that prompts user to enter an integer and prints positive integers
#program stops when a negative integer is entered

def main():
    number = int(input("Please enter an integer: \n"))

    #while loop
    while number > 0 :
        print(number)
        number = int(input("Please enter an integer: \n"))
        
        #conditional to stop loop
        
        if number < 0:
            print("done")



main()
