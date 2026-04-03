def isOdd(number):
    print(type(number))
    print(type(number) == int)
    if type(number) != int:
        return False
    return number % 2 != 0

def isEven(number):
    if type(number) != int:
        return False
    return number % 2 == 0

if __name__ == "__main__" :
    assert isOdd(42) == False
    assert isOdd(9999) == True
    assert isOdd(-10) == False
    assert isOdd(-11) == True
    assert isOdd(0) == False
    assert isEven(42) == True
    assert isEven(9999) == False
    assert isEven(-10) == True
    assert isEven(-11) == False
    assert isEven(3.1415) == False