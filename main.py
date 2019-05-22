import json
import time

with open('words.json') as json_file:
    dics = json.load(json_file)

dics = dics.keys()

boards = [
    ['n', 'ra', 's', 'p'],
    ['s', 'a', 't', 'r'],
    ['k', 'i', 'e', 's'],
    ['s', 'e', 's', 'm']
]
maxLength = 7

w = 4
h = 4

# combine huruf jadi 4 karakter

def findTail(snake, cages, length):
    if len(snake) == length:
        cages.append(snake)
        return

    tail = []
    head = snake[len(snake) - 1]
    y = head[0]
    x = head[1]
    
    if x > 0:
        if [y,x-1] not in snake:
            babySnake = snake.copy()
            babySnake.append([y,x-1])
            findTail(babySnake, cages, length)

    if y > 0:
        if [y-1,x] not in snake:
            babySnake = snake.copy()
            babySnake.append([y-1,x])
            findTail(babySnake, cages, length)

    if x > 0 and y > 0:
        if [y-1,x-1] not in snake:
            babySnake = snake.copy()
            babySnake.append([y-1,x-1])
            findTail(babySnake, cages, length)

    if x < w - 1:
        if [y,x+1] not in snake:
            babySnake = snake.copy()
            babySnake.append([y,x+1])
            findTail(babySnake, cages, length)

    if y < w - 1:
        if [y+1,x] not in snake:
            babySnake = snake.copy()
            babySnake.append([y+1,x])
            findTail(babySnake, cages, length)
        
    if y < w - 1 and x < w - 1:
        if [y+1,x+1] not in snake:
            babySnake = snake.copy()
            babySnake.append([y+1,x+1])
            findTail(babySnake, cages, length)

cages = []
for i in range (0, w):
    for j in range (0, h):
        snake = []
        head = [i,j]
        snake.append(head)
        findTail(snake, cages, maxLength)

for cage in cages:
    word = ''
    for i in cage:
        word += boards[i[0]][i[1]]
    if word in dics:
        print(word)
        # draw board
        ctr = 0
        for i in range (0, w):
            line = ""
            for j in range (0, h):
                checked = False
                for x in cage:
                    if x[0] == i and x[1] == j:
                        ctr+=1
                        checked = True
                        break
                if checked:
                    line += str(ctr)
                else:
                    line += "."
            print(line)
        print("")