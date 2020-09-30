##def main():
##
##    for i in range(-1,-101,-1):
##        print(i)
##
##
##main()

##def main():
##    data = ["hello", 9002, 8, 3.0, 5]
##
##    for i in range(len(data)):
##        print(data[i])
##    i +=1
##
##main()


def spread_strings(list_of_strings):
    i = 0
    spaced_word = " "
    while i < len(list_of_strings):
        spaced_word += list_of_strings[i] + " "
        return spaced_word
    i += 1
        
    
def main():

    list_of_strings = ["Ahh", "This", "WAS", "Difficult"]

    print(spread_strings(list_of_strings))
        
    
        
main()
