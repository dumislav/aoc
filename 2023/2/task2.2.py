import re

def getRounds(gameData):
    return gameData.split('; ')

def roundMinItems(itemSets):
    minItemsSet = {}
    for color, value in itemSets.items():
        if color not in minItemsSet or value < minItemsSet[color]:
            minItemsSet[color] = value
    return minItemsSet

def getRoundItems(roundData):
    items = roundData.split(', ')
    itemSets = {}
    for item in items:
        itemData = item.split(' ')
        itemSets[itemData[1]] = int(itemData[0])
    return itemSets

def gameMinItems(gameData):
    rounds = getRounds(gameData)
    minItems = {}
    for round in rounds:
        roundItems = getRoundItems(round)
        minRoundItems = roundMinItems(roundItems)
        for color, value in minRoundItems.items():
            if color not in minItems or value > minItems[color]:
                minItems[color] = value
    return minItems

    
def main(data):
    rows = data.split('\n')
    rows = filter(None, rows)

    totalSum = 0
    for row in rows:
        gameResult = 1
        print(row)
        regex = re.compile(r'Game\s(\d+):\s(.+)')
        rowData = regex.match(row)
        gameId = rowData[1]
        gameData = rowData[2]
        gameItems = gameMinItems(gameData)
        for color, value in gameItems.items():
            gameResult *= value
        print('Game {}: {}'.format(gameId, gameResult))
        totalSum += gameResult

    return totalSum

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        data = f.read()
        result = main(data)
        print(result)