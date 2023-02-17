
with open('Day 8\Input.txt') as file:
    data = [row.strip() for row in file.readlines()]

ROWS = len(data)
COLUMNS = len(data[0])

#max scenic score
mss = 0

for row in range(1, ROWS-1):
    for column in range(1,COLUMNS-1):
        tree=data[row][column]

        left = [data[row][column-i] for i in range (1, column+1)]
        right = [data[row][column+i] for i in range (1, COLUMNS-column)]
        up = [data[row-i][column] for i in range (1, row+1)]
        down = [data[row+i][column] for i in range(1, ROWS-row)]

        score = 1
        for lst in (left, right, up, down):
            tracker = 0
            for i in range(len(lst)):
                if lst[i] < tree:
                    tracker += 1
                elif lst[i] == tree:
                    tracker += 1
                    break
                else:
                    break
            score *= tracker
            if score > mss:
                mss = score

print(mss)