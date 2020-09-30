import math

def square_each(user_list):
    ''' function: receives list and returns new list with first list values squared
        parameter: one list
        returned list of squared values'''
    
    new_list = []
    index = 0
    for value in user_list:
        new_value = math.pow(user_list[index], 2)
        new_list.append(new_value)
        index += 1

    return new_list
    

    

def main():

    user_list = [3, 5, 7, 9]
    print(user_list)

    print(square_each(user_list))

main()
