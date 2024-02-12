import re

def main(data):
    rows = data.split('\n')

    totalpoints = 0
    arr = []
    row_wins = {}
    round = 0
    for row in rows:
        round += 1
        print(row)
        playtimes = 1
        if len(arr) > 0:
            playtimes += arr[0]
            arr.remove(arr[0])

        cards = 0
        points = 0
        print("Playtime: " + str(playtimes))
        for replay in range(0, playtimes):
            if round in row_wins:
                wins = row_wins[round]
            else:
                numbers = re.finditer(r'\d+', row)
                i = 0
                card = []
                wins = 0
                for number in numbers:
                    if(i > 0 and i <= 10):
                        card.append(int(number.group()))
                    elif(i > 10 and int(number.group()) in card):
                        wins += 1
                    i+=1

                if wins:
                    points += 2**(wins-1)
                row_wins[round] = wins

            for x in range(0, wins):
                if len(arr) > x:
                    arr[x] += 1
                else:
                    arr.append(1)
            cards += 1
        print(wins)
        print(arr)
#        print(points)
        totalpoints += cards
    print(totalpoints)

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        data = f.read()
        main(data)