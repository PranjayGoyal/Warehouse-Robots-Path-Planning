import pygame
import math
from queue import PriorityQueue
from pulp import *
import time
import threading
from collections import OrderedDict

WIDTH = 600
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Warehouse Robots")

RED = (255, 0, 0)
GREEN = (9, 206,55)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
LBLUE = (102, 178, 255)
ROBOT1 = (205, 92, 202)
ROBOT2 = (222, 49, 99)
ROBOT3 = (204, 204, 255)
ROBOT4 = (159, 226, 191)
ROBOT5 = (255, 191, 0)
ROBOT6 = (255, 87, 51)
LGREY = (96,96,96)

class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK or self.color == ORANGE or self.color == LBLUE or self.color == LGREY or self.color==ROBOT1 or self.color==ROBOT2 or self.color==ROBOT3 or self.color==ROBOT4 or self.color==ROBOT5 or self.color==ROBOT6 

    # def is_start(self):
    #     return self.color == ORANGE

    def is_end(self):
        return self.color == GREEN

    def reset(self):
        self.color = WHITE

    def make_start1(self):
        self.color = ROBOT1

    def make_start2(self):
        self.color = ROBOT2

    def make_start3(self):
        self.color = ROBOT3

    def make_start4(self):
        self.color = ROBOT4

    def make_start5(self):
        self.color = ROBOT5

    def make_start6(self):
        self.color = ROBOT6

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_rep(self):
        self.color = ORANGE

    def make_del(self):
        self.color = LBLUE

    def make_cs(self):
        self.color = LGREY

    def make_end(self):
        self.color = GREEN

    def make_path1(self):
        self.color = ROBOT1

    def make_path2(self):
        self.color = ROBOT2

    def make_path3(self):
        self.color = ROBOT3

    def make_path4(self):
        self.color = ROBOT4

    def make_path5(self):
        self.color = ROBOT5

    def make_path6(self):
        self.color = ROBOT6

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        # DOWN
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])

        # UP
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():  
            self.neighbors.append(grid[self.row - 1][self.col])

        # rt
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])

        # lt
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():  
            self.neighbors.append(grid[self.row][self.col - 1])

        # upper lt
        if (self.col > 0 and self.row > 0) and not grid[self.row-1][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row-1][self.col - 1])

        # upper rt
        if (self.row < self.total_rows-1 and self.col > 0) and not grid[self.row+1][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row+1][self.col - 1])

        # lower lt
        if (self.col < self.total_rows-1 and self.row > 0) and not grid[self.row-1][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row-1][self.col + 1])

        # lower rt
        if (self.col < self.total_rows-1 and self.row < self.total_rows-1) and not grid[self.row+1][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row+1][self.col + 1])

    def _lt_(self, other):
        return False


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)




def reconstruct_path2(came_from, current, draw, robotNo,final,begin,thread_name,end,grid,nnn):
    
    res=[]
    while current in came_from:
        current = came_from[current]
        res.append(current)
    res1=res[::-1]
    res1.append(final)

    for curr in res1:
        if curr==begin:
            curr.color=WHITE
        f=False

        if curr.color == GREEN and curr != final:
            f=True

        if curr.is_barrier():
            continue
               
        if(robotNo == 1):
            if curr.color!=GREEN:
                curr.make_path1()
            if curr==final:
                curr.make_path1()
            
        elif(robotNo == 2):
            if curr.color!=GREEN:
                curr.make_path2()
            if curr==final:
                curr.make_path2()
           
        elif(robotNo == 3):
            if curr.color!=GREEN:
                curr.make_path3()
            if curr==final:
                curr.make_path3()
             
        elif(robotNo == 4):
            if curr.color!=GREEN:
                curr.make_path4()
            if curr==final:
                curr.make_path4()    
            
        elif(robotNo == 5):
            if curr.color!=GREEN:
                curr.make_path5()
            if curr==final:
                curr.make_path5()
            
        elif robotNo == 6 :
            if curr.color!=GREEN:
                curr.make_path6()
            if curr==final:
                curr.make_path6()
             
        time.sleep(0.3)
        draw()
        if curr!=final:
            curr.color=WHITE

        if f==True:
            curr.color = GREEN    

        pygame.display.update()
         
    if nnn==0:
        algorithm2(thread_name,draw,grid,final,end,robotNo,1)       

def algorithm2(thread_name,draw, grid, start, end, robotNo,i):
    
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end[i].get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end[i]:
            
            reconstruct_path2(came_from, end[i], draw, robotNo,end[i],start,thread_name,end,grid,i)
            return True

        for neighbor in current.neighbors:
            if(neighbor == grid[current.row + 1][current.col] or neighbor == grid[current.row][current.col +1] or neighbor ==grid[current.row - 1][current.col] or neighbor == grid[current.row][current.col-1]):
                temp_g_score = g_score[current] + 1
            else:
                temp_g_score = g_score[current] + 1.4
            

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end[i].get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    # neighbor.make_open()

        draw()
    return False


def algorithm(grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            return f_score[end]

        for neighbor in current.neighbors:
            if(neighbor == grid[current.row + 1][current.col] or neighbor == grid[current.row][current.col +1] or neighbor ==grid[current.row - 1][current.col] or neighbor == grid[current.row][current.col-1]):
                temp_g_score = g_score[current] + 1
            else:
                temp_g_score = g_score[current] + 1.4

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col



def main(win, width):
    ROWS = 40
    grid = make_grid(ROWS, width)
    gap = width // ROWS
    start1 = grid[1][17]
    start1.make_start1()
    end1 = None
    start2 = grid[1][18]
    start2.make_start2()
    end2 = None
    start3 = grid[1][19]
    start3.make_start3()
    end3 = None
    start4 = grid[1][20]
    start4.make_start4()
    end4 = None
    start5 = grid[1][21]
    start5.make_start5()
    end5 = None
    start6 = grid[1][22]
    start6.make_start6()
    end6 = None

    run = True

    while run:
        draw(win, grid, ROWS, width)
        for row in range(40):
            for column in range(40):
                
                if (row == 4 or row == 5 or row == 9 or row == 10 or row == 14 or row == 15 or row == 19 or row == 20 or row == 24 or row == 25 or row == 29 or row == 30 or row == 34 or row == 35) and (column == 4 or column == 5 or column == 6 or column == 7 or column == 11 or column == 12 or column == 13 or column == 14 or column == 18 or column == 19 or column == 20 or column == 21 or column == 25 or column == 26 or column == 27 or column == 28 or column == 32 or column == 33 or column == 34 or column == 35):
                    sp = grid[column][row]
                    sp.make_barrier()
                if(row == 0 or row == 39) and (column == 7 or column == 8 or column == 9 or column == 10 or column == 11 or column == 28 or column == 29 or column == 30 or column == 31 or column == 32):
                    sp = grid[column][row]
                    sp.make_rep()
                if((row == 0) and (column == 7 or column == 8 or column == 9 or column == 10 or column == 11)) or ((row == 39) and (column == 28 or column == 29 or column == 30 or column == 31 or column == 32)):
                    sp = grid[column][row]
                    sp.make_del()
                if((row == 17 or row == 18 or row == 19 or row == 20 or row == 21 or row == 22) and (column == 0)):
                    sp = grid[column][row]
                    sp.make_cs()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # lt
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start1 and spot != start2 and spot != start3 and spot != start4 and spot != start5 and spot != start6 and spot != end1 and spot != end2 and spot != end3 and spot != end4 and spot != end5 and spot != end6:
                    start1 = spot
                    start1.make_start1()

                elif not start2 and spot != start1 and spot != start3 and spot != start4 and spot != start5 and spot != start6 and spot != end1 and spot != end3 and spot != end4 and spot != end5 and spot != end6:
                    start2 = spot
                    start2.make_start2()

                elif not start3 and spot != start2 and spot != start1 and spot != start4 and spot != start5 and spot != start6 and spot != end1 and spot != end3 and spot != end4 and spot != end5 and spot != end6:
                    start3 = spot
                    start3.make_start3()

                elif not start4 and spot != start2 and spot != start3 and spot != start1 and spot != start5 and spot != start6 and spot != end1 and spot != end3 and spot != end4 and spot != end5 and spot != end6:
                    start4 = spot
                    start4.make_start4()

                elif not start5 and spot != start2 and spot != start3 and spot != start4 and spot != start1 and spot != start6 and spot != end1 and spot != end3 and spot != end4 and spot != end5 and spot != end6:
                    start5 = spot
                    start5.make_start5()

                elif not start6 and spot != start2 and spot != start3 and spot != start4 and spot != start5 and spot != start1 and spot != end1 and spot != end3 and spot != end4 and spot != end5 and spot != end6:
                    start6 = spot
                    start6.make_start6()

                elif not end1 and spot != start2 and spot != start3 and spot != start4 and spot != start5 and spot != start6 and spot != start1 and spot != end3 and spot != end4 and spot != end5 and spot != end6:
                    end1 = spot
                    end1.make_end()

                elif not end2 and spot != start2 and spot != start3 and spot != start4 and spot != start5 and spot != start6 and spot != end1 and spot != end3 and spot != end4 and spot != end5 and spot != end6:
                    end2 = spot
                    end2.make_end()

                elif not end3 and spot != start2 and spot != start3 and spot != start4 and spot != start5 and spot != start6 and spot != end1 and spot != end2 and spot != end4 and spot != end5 and spot != end6:
                    end3 = spot
                    end3.make_end()

                elif not end4 and spot != start2 and spot != start3 and spot != start4 and spot != start5 and spot != start6 and spot != end1 and spot != end3 and spot != end2 and spot != end5 and spot != end6:
                    end4 = spot
                    end4.make_end()

                elif not end5 and spot != start2 and spot != start3 and spot != start4 and spot != start5 and spot != start6 and spot != end1 and spot != end3 and spot != end4 and spot != end2 and spot != end6:
                    end5 = spot
                    end5.make_end()

                elif not end6:
                    end6 = spot
                    end6.make_end()

            # elif pygame.mouse.get_pressed()[2]:  # rt
            #     pos = pygame.mouse.get_pos()
            #     row, col = get_clicked_pos(pos, ROWS, width)
            #     spot = grid[row][col]
            #     spot.reset()
            #     if spot == start:
            #         start = None
            #     elif spot == end:
            #         end = None

            if event.type == pygame.KEYDOWN:
                    
                if event.key == pygame.K_SPACE and start1 and start2 and start3 and start4 and start5 and start6 and end1 and end2 and end3 and end4 and end5 and end6:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                    start = [start1, start2, start3, start4, start5, start6]
                    end = [end1, end2, end3, end4, end5, end6]
                    print(end[0].row)
                    costMatrix = []
                    for i in range(0,6):
                        a = []
                        for j in range(0,6):
                            pygame.display.update()  
                            a.append(algorithm(grid, start[i], end[j]))
                            print(algorithm(grid, start[i], end[j]))
                        costMatrix.append(a)

                    print(costMatrix)

                    costMatrix2 = []
                    for i in range(0,6):
                        a = []
                        for j in range(0,6):
                            pygame.display.update()  
                            a.append(algorithm(grid, end[i], end[j]))
                            print(algorithm(grid, end[i], end[j]))
                        costMatrix2.append(a)

                    print(costMatrix2)

                    end1M = [end1,end2]
                    end3M = [end3,end4]
                    end5M = [end5,end6]
                    
                    robots = [1, 2, 3, 4, 5, 6]
                    tasks = [1, 2, 3, 4, 5, 6]

                    prob = LpProblem("Assignment Problem", LpMinimize)
                    costs = makeDict([robots, tasks], costMatrix, 0)

                    # Creates a list of tuples containing all the possible assignments
                    assign = [(w, j) for w in robots for j in tasks]

                    # A dictionary called 'Vars' is created to contain the referenced variables
                    vars = LpVariable.dicts(
                    "Assign", (robots, tasks), 0, None, LpBinary)
                    prob += (lpSum([vars[w][j] * costs[w][j]for (w, j) in assign]), "Sum_of_Assignment_Costs")
                    for j in robots:
                        prob += lpSum(vars[w][j] for w in robots) == 1

                    # There are column constraints. Each employee can be assigned to only one job.
                    for w in tasks:
                        prob += lpSum(vars[w][j] for j in tasks) == 1

                    prob.solve()

                    for v in prob.variables():
                        print(v.name, "=", v.varValue)

                    print("Value of Objective Function = ", value(prob.objective))

                    final = []
                    # Print the variables oplainTextimized value
                    for v in prob.variables():
                        if v.varValue != 0:
                            final.append(int(v.name[9]))

                    for i in range(0,  len(final)):
                        print(final[i])

                    thread1 = threading.Thread(target=algorithm2, 
                           args=("thread1",lambda: draw(win, grid, ROWS, width),
                               grid, start[0], end1M, 1,0 ))         
                    thread2 = threading.Thread(target=algorithm2, 
                           args=("thread2",lambda: draw(win, grid, ROWS, width),
                               grid, start[1], end3M, 2,0 ))  
                    thread3 = threading.Thread(target=algorithm2, 
                           args=("thread3",lambda: draw(win, grid, ROWS, width),
                               grid, start[5], end5M, 6,0 ))  
                    # thread4 = threading.Thread(target=algorithm2, 
                    #        args=("thread4",lambda: draw(win, grid, ROWS, width),
                    #            grid, start[3], end[final[3]-1], 4 ))  
                    # thread5 = threading.Thread(target=algorithm2, 
                    #        args=("thread5",lambda: draw(win, grid, ROWS, width),
                    #            grid, start[4], end[final[4]-1], 5 ))             
                    # thread6 = threading.Thread(target=algorithm2, 
                    #        args=("thread6",lambda: draw(win, grid, ROWS, width),
                    #            grid, start[5], end[final[5]-1], 6 ))  


                    thread1.start()
                    thread2.start()
                    thread3.start()
                    # thread4.start()
                    # thread5.start()
                    # thread6.start()
  

                    thread1.join()
                    thread2.join()
                    thread3.join()
                    # thread4.join()
                    # thread5.join()
                    # thread6.join()
                
                    #time.sleep(0.1)
                    start1 = end1M[1]
                    start2 = end3M[1]
                    start6 = end5M[1]
                    # start4 = end[final[3]-1]
                    # start5 = end[final[4]-1]
                    # start6 = end[final[5]-1]
                    end1=None
                    end2=None
                    end3=None
                    end4=None
                    end5=None
                    end6=None
    pygame.quit()
main(WIN, WIDTH)

