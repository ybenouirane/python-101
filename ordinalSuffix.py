def ordinalSuffix(number):
        if(number % 10 == 1 and number != 11):
            return f"{number}st"
        elif (number % 10 == 2 and number != 12):
            return f"{number}nd"
        elif (number % 10 == 3 and number != 13):
            return f"{number}rd"
        else:
            return f"{number}th"
        
if __name__ == "__main__":
    for i in range(100):
        print(ordinalSuffix(i))
