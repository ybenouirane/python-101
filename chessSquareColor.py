def getChessSquareColor(column, row):
    if column > 8 or row > 8 or column < 1 or row < 1:
        return ''
    if column % 2 == row % 2 == 0:
        return 'white'
    else:
        return 'black'
