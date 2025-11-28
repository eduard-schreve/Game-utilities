import math

class follow:
    angle = 0
    def __init__(self, speed):
        self.vect = [0, 0]
        self.start = [0, 0]
        self.end = [0, 0]
        self.speed = speed

    def linear(self, start, end):
        self.start = start
        self.end = end

        self.vect = [self.start[0] - self.end[0], self.start[1] - self.end[1]]
        minus = [self.vect[0] / abs(self.vect[0]) , self.vect[1] / abs(self.vect[1])]
        self.vect = [self.speed, math.atan(self.vect[0] / self.vect[1])]
        self.vect = [self.vect[0] * math.cos(self.vect[1]), self.vect[0] * math.sin(self.vect[1])]

        self.vect = [self.vect[0] * -minus[0], self.vect[1] * -minus[1]]

        return self.vect

    def circular(self, center, radius, degrees = 360):

        self.vect[0] = center[0] + radius * math.cos(math.radians(follow.angle))
        self.vect[1] = center[1] + radius * math.sin(math.radians(follow.angle))

        if follow.angle <= degrees or degrees == 360:
            follow.angle += self.speed

        return self.vect

def aStar(grid, start, end, atEnd = False):
    curnode = start
    path = []

    h = math.sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)
    g = 0
    f = g + h
    openNodes = []
    fNodes = []

    while not atEnd:
        atEnd = False
        if curnode[0] == end[0] and curnode[1] == end[1]:
            atEnd = True

        prevNode = curnode
        #-FIND THE NEGIBOURS AND ASSIGN THE OPEN NODES-#
        #-TOP-#
        curnode = [prevNode[0], prevNode[1] - 1]
        if curnode[1] != 0:
            if not (grid[curnode[0]][curnode[1]] == 1):
                h = math.sqrt((curnode[0] - end[0]) ** 2 + (curnode[1] - end[1]) ** 2)
                g = 1
                f = g + h
                openNodes.append([f, g, h, curnode, prevNode])
                fNodes.append(f)

        #-TOP RIGHT-#
        curnode = [prevNode[0] + 1, prevNode[1] - 1]
        if curnode[1] != 0 and curnode[0] != len(grid[0]):
            if not (grid[curnode[0]][curnode[1]] == 1):
                h = math.sqrt((curnode[0] - end[0]) ** 2 + (curnode[1] - end[1]) ** 2)
                g = 1.41
                f = g + h
                openNodes.append([f, g, h, curnode, prevNode])
                fNodes.append(f)
        
        #-RIGHT-#
        curnode = [prevNode[0] + 1, prevNode[1]]
        if curnode[0] != len(grid[0]):
            if not (grid[curnode[0]][curnode[1]] == 1):
                h = math.sqrt((curnode[0] - end[0]) ** 2 + (curnode[1] - end[1]) ** 2)
                g = 1
                f = g + h
                openNodes.append([f, g, h, curnode, prevNode])
                fNodes.append(f)
        
        #-BOTTOM RIGHT-#
        curnode = [prevNode[0] + 1, prevNode[1] + 1]
        if curnode[0] != len(grid[0]) and curnode[1] != len(grid):
            if not (grid[curnode[0]][curnode[1]] == 1):
                h = math.sqrt((curnode[0] - end[0]) ** 2 + (curnode[1] - end[1]) ** 2)
                g = 1.41
                f = g + h
                openNodes.append([f, g, h, curnode, prevNode])
                fNodes.append(f)
        
        #-BOTTOM-#
        curnode = [prevNode[0], prevNode[1] + 1]
        if curnode[1] != len(grid):
            if not (grid[curnode[0]][curnode[1]] == 1):
                h = math.sqrt((curnode[0] - end[0]) ** 2 + (curnode[1] - end[1]) ** 2)
                g = 1
                f = g + h
                openNodes.append([f, g, h, curnode, prevNode])
                fNodes.append(f)
        
        #-BOTTOM LEFT-#
        curnode = [prevNode[0] - 1, prevNode[1] + 1]
        if curnode[0] != 0 and curnode[1] != len(grid):
            if not (grid[curnode[0]][curnode[1]] == 1):
                h = math.sqrt((curnode[0] - end[0]) ** 2 + (curnode[1] - end[1]) ** 2)
                g = 1.41
                f = g + h
                openNodes.append([f, g, h, curnode, prevNode])
                fNodes.append(f)
        
        #-LEFT-#
        curnode = [prevNode[0] - 1, prevNode[1]]
        if curnode[0] != 0 :
            if not (grid[curnode[0]][curnode[1]] == 1):
                h = math.sqrt((curnode[0] - end[0]) ** 2 + (curnode[1] - end[1]) ** 2)
                g = 1
                f = g + h
                openNodes.append([f, g, h, curnode, prevNode])
                fNodes.append(f)
        
        #-TOP LEFT-#
        curnode = [prevNode[0] - 1, prevNode[1] - 1]
        if curnode[0] != 0 and curnode[1] != 0:
            if not (grid[curnode[0]][curnode[1]] == 1):
                h = math.sqrt((curnode[0] - end[0]) ** 2 + (curnode[1] - end[1]) ** 2)
                g = 1.41
                f = g + h
                openNodes.append([f, g, h, curnode, prevNode])
                fNodes.append(f)

        # print(openNodes)
        curnode = openNodes[fNodes.index(min(fNodes))][3]

        path.append(curnode)

        print("path: " + str(path))
        # print(curnode)
        # print(atEnd)

    return path
    