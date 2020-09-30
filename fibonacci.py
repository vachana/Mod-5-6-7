def fibonacci(length):

    i = 0
    a = 0
    b = 1
    while i < length:
        print(a)
        c = a + b
        a = b 
        b = c
        i += 1
        

    



def main():

    length = int(input("Please enter a number: "))

    print(fibonacci(length))


main()

    
        
