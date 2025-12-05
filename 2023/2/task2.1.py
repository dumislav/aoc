import re
itemInBag = {'red': 12, 'green': 13, 'blue': 14}

def checkItemInBag(items):
    for item in items:
        itemData = item.split(' ')
        if int(itemInBag[itemData[1]]) < int(itemData[0]):
            return False
    return True


def main(data):
    rows = data.split('\n')
    rows = filter(None, rows)
    sumGameIds = 0
    for row in rows:
        print(row)
        regex = re.compile(r'Game\s(\d+):\s(.+)')
        rowData = regex.match(row)
        gameId = rowData[1]
        gameData = rowData[2].split('; ')
        gameRoundBr = 0
        validGame = True
        for gameRound in gameData:
            gameRoundBr += 1
            items = gameRound.split(', ')
            if not checkItemInBag(items):
                validGame = False
                break
        if validGame:
            sumGameIds += int(gameId)

        print('Game {}: {}'.format(gameId, 'OK' if validGame else 'INVALID'))

    print('Sum of valid game ids: {}'.format(sumGameIds))

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        data = f.read()
        main(data)