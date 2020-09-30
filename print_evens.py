def print_evens(start):
    ''' function: counts by two from a starting number to 100 inclusive
        parameters: starting number
        returns: printed counting by twos from start to 100'''
    
    start = 0

    while start < 99:
        start += 2
        print(start)

def main():
    count_from = 0

    print_evens(count_from)
    




main()
