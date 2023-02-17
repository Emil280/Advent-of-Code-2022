
with open('Day 8\Input.txt') as file:
    data = [row.strip() for row in file.readlines()]

ROWS = len(data)
COLUMNS = len(data[0])

edges = (ROWS * 2) + ((COLUMNS-2)*2)
total = edges

for row in range(1, ROWS-1):
    for column in range(1,COLUMNS-1):
        tree=data[row][column]

        left = [data[row][column-i] for i in range (1, column+1)]
        right = [data[row][column+i] for i in range (1, COLUMNS-column)]
        up = [data[row-i][column] for i in range (1, row+1)]
        down = [data[row+i][column] for i in range(1, ROWS-row)]
        
        if max(left) < tree or max(right) < tree or max(up) < tree or max(down) < tree:
            total += 1

print(total)