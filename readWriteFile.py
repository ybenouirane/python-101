def writeToFile(filename, txt):
    with open(filename, 'w') as fileObj:
        fileObj.write(txt)

def appendToFile(filename, txt):
    with open(filename, 'a') as fileObj:
        fileObj.write(txt)

def readFromFile(filename):
    with open(filename, 'r') as fileObj:
        return fileObj.read()

if __name__ == "__main__":
    writeToFile('greet.txt', 'Hello!\n')
    appendToFile('greet.txt', 'Goodbye!\n')
    assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'
