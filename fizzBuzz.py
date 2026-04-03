def fizzBuzz(upTo):
    for i in range(upTo):
        print(str(i).rjust(2), i % 3, i % 5)
        if (i % 3 == 0 and upTo % 5 == 0):
            print('FizzBuzz')
        elif (i % 3 == 0):
            print('Fizz')
        elif (i % 5 == 0):
            print('Buzz')
        else:
            print()

    
if __name__ == "__main__":
    fizzBuzz(20)