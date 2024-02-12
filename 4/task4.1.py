import re

def main(data):
    rows = data.split('\n')

    totalpoints = 0
    for row in rows:
        points = 0

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

        totalpoints += points
    print(totalpoints)

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        data = f.read()
        main(data)