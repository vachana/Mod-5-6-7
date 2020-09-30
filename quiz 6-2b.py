def max_value(number_list):
    
    current_max_number = number_list[0]
    
    for number in number_list:
        if number > current_max_number:
            current_max_number = number
    

    return current_max_number

def main():
    
    number_list = [93, 10004, 2, -3, 6]

    print(max_value(number_list))



main()
        
