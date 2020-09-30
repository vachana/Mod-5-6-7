#program that reads back the user's input of a word and stops if 'stop' is entered

def main():
    word_list = [] #empty list
    
    word = input("Enter a word: ")
    while word != "stop":
        word_list.append(word)
        word = input("Enter a word: ")
        
        if word == "stop":
            print(word_list)
            
            
    #not sure how to store user input if not using a list that is adding onto itself

main()

