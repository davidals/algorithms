"""
A robot is located at the top-left corner of a 4x4 grid. 
The robot can move either up, down, left, or right, but can not visit the same spot twice. 
The robot is trying to reach the bottom-right corner of the grid.

Print out the unique number of ways the robot can reach its destination
"""
class RobotMovement:
    def __init__(self, height, width):
        self.visited = {}
        self.height = height
        self.width = width
        self.count = 0;
        for i in range(self.height):
            for j in range(self.width):
                self.visited[(i,j)] = False
                
    def findPaths(self, position):
        if(position == (self.height -1, self.width -1)):
            self.count +=  1
            
        if (not self.visited[position]):
            self.visited[position] = True
            for pos in self.availablePositions(position):
                self.findPaths(pos)
            self.visited[position] = False

    def availablePositions(self, startingPoint):
        result = []
        top = (startingPoint[0] - 1, startingPoint[1])
        bottom = (startingPoint[0] + 1, startingPoint[1])
        left = (startingPoint[0], startingPoint[1] - 1)
        right = (startingPoint[0], startingPoint[1] + 1)
        
        result.append(top)
        result.append(bottom)
        result.append(left)
        result.append(right)
        
        result = [x for x in result if self.isValid(x)]
        return result

    def isValid(self, position):
        valid = position[0] >= 0 and position[0] < self.height and position[1] >= 0 and position[1] < self.width;
        return valid

r = RobotMovement(4,4)
r.findPaths((0,0))

print r.count
