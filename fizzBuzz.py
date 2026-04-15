def fizzBuzz(upTo):
    for i in range(upTo):
        if (i % 3 == 0 and i % 5 == 0):
            print('FizzBuzz', i)
        elif (i % 3 == 0):
            print('Fizz', i)
        elif (i % 5 == 0):
            print('Buzz', i)
        else:
            print('none of them', i)

if __name__ == "__main__":
    fizzBuzz(20)