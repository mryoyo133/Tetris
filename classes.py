from turtle import width
import pygame
import time

pygame.init()

width = 50


class GridBlock():
    def __init__(self, x, y, width, height, thickness, color, win, empty):
        self.x = x
        self.y = y 
        self.width = width
        self.height = height
        self.color = color
        self.win = win
        self.thickness = thickness
        self.empty = empty
    def draw(self):
        pygame.draw.rect(self.win, self.color, pygame.Rect((self.x+4)*50, self.y*50, self.width, self.height), self.thickness)

class Block():
    def __init__(self, x, y, width, color, win):
        self.x = x
        self.y = y 
        self.width = width
        self.color = color
        self.win = win

    def draw(self):
        pygame.draw.rect(self.win, self.color, pygame.Rect((self.x+4)*50, self.y*50, self.width, self.width))  

    def movedown(self):
        self.y += 1    
    
    def static(self):
        if self.y == 15:
            return True
        return False    

class TwoByTwoBlock():
    def __init__(self, x, y, width, color, blocks, win):
        self.x = x
        self.y = y
        self.width = width
        self.color = color
        self.blocks = blocks
        self.win = win
        
        block1 = Block(self.x, self.y, width, self.color, win)
        block2 = Block(self.x + 1, self.y, width, self.color, win)
        block3 = Block(self.x, self.y + 1, width, self.color, win)
        block4 = Block(self.x + 1, self.y + 1, width, self.color, win)

        blocks.append(block1)
        blocks.append(block2)
        blocks.append(block3)
        blocks.append(block4)

    def movedown(self):
        for block in self.blocks:
            block.movedown()
        self.y += 1    

    def draw(self):
        for block in self.blocks:
            block.draw()

    def static(self):
        for block in self.blocks:
            if block.static():
                return True

        return False                           

    def moveright(self):
        if self.x != 8:
            self.x += 1
            for block in self.blocks:
                block.x += 1
                
    def movelift(self):
        if self.x != 0:
            self.x -= 1

            for block in self.blocks:
                block.x -= 1                

