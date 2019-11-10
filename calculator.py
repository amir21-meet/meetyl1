from turtle import Turtle
class Ball(Turtle):
        def __init__(self, radius, color, dx, dy):
            Turtle.__init__(self)
            self.radius = radius
            self.color = color
            self.dx = dx
            self.dy = dy
            self.shape(Circle)
            self.color(red)
            self.size(r/10)        
