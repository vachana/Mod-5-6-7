def count_down():
    for i in range(100, 1, -5):
        print(i)

#cant get to run if i switch out my print statement for a return
#prints "none" before blastoff
def main():

    print(count_down())
    print("Blastoff!")

main()
