import random

maze = []

maze_edges = {}

def clear_maze():
    global maze
    maze = [['#' for i in range(7)] for j in range(7)]
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if i % 2 != 0 and j % 2 != 0:
                maze[i][j] = "."

def make_dict():
    for i in range(3):
        for j in range(3):
            maze_edges[(i,j)]=[]

def prims():
    cells = [['#' for i in range(3)] for j in range(3)]
    point = (random.randint(0,2), random.randint(0,2))
    frontiers = []
    checked = []
    frontiers.append(point)
    while frontiers:
        point=random.choice(frontiers)
        i = point[0]
        j = point[1]
        moves = []
        if i > 0:
            moves.append((i-1,j))
        if i < len(cells)-1:
            moves.append((i+1,j))
        if j > 0:
            moves.append((i,j-1))
        if j < len(cells[i])-1:
            moves.append((i,j+1))
        done_moves = []
        move = random.choice(moves)
        while point in maze_edges[move]:
            done_moves.append(move)
            move = random.choice(moves)
            equal = True
            for not_done in moves:
                if not_done not in done_moves:
                    equal = False
                    break
            if equal:
                break
        maze_edges[point].append(move)
        edge_i = move[0]-point[0]
        edge_j = move[1]-point[1]
        if edge_i == 0:
            maze[point[0]*2+1][point[1]*2+edge_j+1]="."
        elif edge_j == 0:
            maze[point[0]*2+edge_i+1][point[1]*2+1]="."
        frontiers.remove(point)
        checked.append(point)
        for m in moves:
            if m not in frontiers and m not in checked:
                frontiers.append(m)
        
def print_maze():
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            print(maze[i][j], end="")
        print()

clear_maze()
make_dict()
prims()
print_maze()
