def main():
    user_sentence = input("Please enter your sentence: ")

    user_list = user_sentence.split()
    number = 0
    for i, words in enumerate(user_list):
        print(i, ". ", words)
    



main()
