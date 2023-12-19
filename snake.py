import turtle
class Snake:
    def __init__(self):
        self.position = [(0, 0), (-20, 0), (-40, 0)]
        self.squares = []
        for i in self.position:
            square = turtle.Turtle()
            square.shape('square')
            square.color('white')
            square.penup()
            square.goto(i)
            self.squares.append(square)
    def grow(self):
        square = turtle.Turtle()
        square.goto(self.squares[-1].position())
        square.shape('square')
        square.color('white')
        square.penup()
        self.squares.append(square)
    def move(self):
        for squ_number in range(len(self.squares) - 1, 0, -1):
            x = self.squares[squ_number - 1].xcor()
            y = self.squares[squ_number - 1].ycor()
            self.squares[squ_number].goto(x, y)
        self.squares[0].forward(20)

    def left(self):
        self.squares[0].left(90)

    def right(self):
        self.squares[0].right(90)