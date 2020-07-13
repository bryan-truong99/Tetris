import random


#Class that defines Tetris Figures
class Figure:

    #Variable that contains list of shapes and their different permutations
    #Based on a matrix
    #First row - Straight line shape
    #Second row - L shape
    #Third row - Backwards L shape
    #Fourth row - Z shape
    #Fifth row - Backwards z shape
    #Sixth row - Square shape
    figures=[
        [[2, 6, 10, 14], [8, 9, 10, 11]],
        [[1, 5, 9, 10], [4, 5, 6, 8], [0, 1, 5, 9], [2, 4, 5, 6]],
        [[2, 6, 9, 10], [1, 5, 6, 7], [2, 3, 6, 10], [5, 6, 7, 11]],
        [[5, 6, 10, 11], [6, 9, 10, 13]],
        [[5, 6, 8, 9], [4, 8, 9, 13]],
        [[5, 6, 9, 10]]
     ]

     #Constructor of Figure class
     def __init__(self, x, y):
         self.x = x
         self.y = y
         self.type = random.randint(0, len(self.figures)-1)
         self.color = random.randint(1, len(colors)-1)
         self.rotation = 0

    #Returns the figure specific to type and rotation specified
    def image(self):
        return self.figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation+1) % len(self.figures[self.type])
