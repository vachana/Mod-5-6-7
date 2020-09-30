def max_value(user_list):
    user_list = []
    i = 0
    for i in range(len(user_list)):
        if user_list[i] > user_list[i + 1]:
            user_list[i] = user_list[i]

        else:
            user_list[i] = user_list[i + 1]
        i += 1
    
    return user_list

def main():
    my_list = [95, 10004, 4, 8, 93]

    print(max_value(my_list))

main()
