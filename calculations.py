def main():
    #user input on how many integers, what integers, and returns the sum and average

    number_of_integers = int(input("Enter the number of values to read: "))

    integer_values = 0
    values_entered = []
    
    while integer_values < number_of_integers:
        ask_for_values = int(input("please enter your integer: "))
        integer_values += 1
        values_entered.append(ask_for_values)

    #find sum and average using python tools and our list
        
    sum_of_values = sum(values_entered)
    average_of_values = sum(values_entered)/len(values_entered)
    
    print("The sum is ",sum_of_values)
    print("The average is ", average_of_values)
    

    


main()
