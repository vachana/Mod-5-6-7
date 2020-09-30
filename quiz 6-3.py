


def spread_strings(word):
    index = 0
    spaced_word = ""
    while (index < len(word)):
        spaced_word += word[index] + "   " 
        index += 1
    return spaced_word
        



        
    
def main():
    
    word_list= ["Hello", "howdy", "Hiya"]
    word_one_list = word_list[0]
    word_two_list = word_list[1]
    word_three_list = word_list[2]
    
    print(spread_strings(word_one_list))
    print(spread_strings(word_two_list))
    print(spread_strings(word_three_list))



main()
          
