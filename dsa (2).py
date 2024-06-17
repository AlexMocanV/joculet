import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze")
wn.setup(1000, 1000)
wn.tracer(0)

class Maze(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.tiltangle(90)
        self.gold = 0

    def up(self):
        if (self.xcor(), self.ycor() + 50) not in pereti:
            self.goto(self.xcor(), self.ycor() + 50)

    def down(self):
        if (self.xcor(), self.ycor() - 50) not in pereti:
            self.goto(self.xcor(), self.ycor() - 50)

    def right(self):
        if (self.xcor() + 50, self.ycor()) not in pereti:
            self.goto(self.xcor() + 50, self.ycor())

    def left(self):
        if (self.xcor() - 50, self.ycor()) not in pereti:
            self.goto(self.xcor() - 50, self.ycor())

    def is_comoara(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        return math.sqrt(a**2 + b**2) < 20

inamiciii = []

class Comoara(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.gold = 100

    def colectat(self):
        self.goto(3000, 3000)
        self.hideturtle()

class Inamic(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.directie = random.choice(["up", "down", "left", "right"])

    def move(self):
        if self.directie == "up":
            dx = 0
            dy = 50
        elif self.directie == "down":
            dx = 0
            dy = -50
        elif self.directie == "left":
            dx = -50
            dy = 0
        elif self.directie == "right":
            dx = 50
            dy = 0

        x = self.xcor() + dx
        y = self.ycor() + dy

        if (x, y) not in pereti:
            self.goto(x, y)
        else:
            self.directie = random.choice(["up", "down", "left", "right"])

        turtle.ontimer(self.move, t=random.randint(100, 300))

levels = [" "]
nivelul_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "X  XXXXX XXXXXXX  XXXXXXCXXX",
    "XX X    X XXXXXX X    X  XXX",
    "XX   XX   XXXXXE   XX   XXXX",
    "X         XXXXX         XXXX",
    "X         XXXX          EXXX",
    "XX XXXEX          XXXX   XXX",
    "X    XXXXXXXXXX    XXXXXXXXX",
    "XXXX XXXXXX  XXXEX XXXXXX  X",
    "XXX  XXXXXXXXXXXX  XXXXXXXXX",
    "XX    XXE    XX    XXXXXX XX",
    "XXX XXX  XXX     XXXXXXXXXXX",
    "XXP                 XXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]
nivelul_2 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XC  XXXX XXXXXXX  XXXXXXPXXX",
    "X  X    X XXXXXX X    X  XXX",
    "XX X XX   XXXXXX   XX   XXXX",
    "X  X X    XXXXXX         XXX",
    "X    XXX   XXX          XXXX",
    "XX XXXXX          XXXX   XXX",
    "X    XXX  XXXXX    XXXXXXXXX",
    "XXX  XXXX X  XXXXX XXXXXX  X",
    "XXX  XXXX XXXXXXX  XXXXXXXXX",
    "XX    XXX    XX    XXXXXX XX",
    "XXX  XX  XXX     XXXXXXX   X",
    "XXX                 XXX    X",
    "XXXXXXXXXXXXXXXXXXXXXXX   XX",
]

levels.append(nivelul_1)
levels.append(nivelul_2)

pereti = []
comori = []

def setup_maze(level):
    wn.bgcolor("black")
    player.showturtle()
    for y in range(len(level)):
        for x in range(len(level[y])):
            coordonate_x = -700 + (x * 50)
            coordonate_y = 300 - (y * 50)
            if level[y][x] == "X":
                patrate.goto(coordonate_x, coordonate_y)
                patrate.stamp()
                pereti.append((coordonate_x, coordonate_y))
            if level[y][x] == "P":
                player.goto(coordonate_x, coordonate_y)
            if level[y][x] == "C":
                comori.append(Comoara(coordonate_x, coordonate_y))
            if level[y][x] == "E":
                inamiciii.append(Inamic(coordonate_x, coordonate_y))

patrate = Maze()
player = Player()

turtle.listen()
turtle.onkey(player.up, "Up")
turtle.onkey(player.down, "Down")
turtle.onkey(player.left, "Left")
turtle.onkey(player.right, "Right")
turtle.onkey(player.up, "w")
turtle.onkey(player.down, "s")
turtle.onkey(player.left, "a")
turtle.onkey(player.right, "d")

setup_maze(levels[1])

wn.tracer(0)

for inamic in inamiciii:
    turtle.ontimer(inamic.move, t=350)
    
while True:
    for comoara in comori:
        if player.is_comoara(comoara):
            player.gold += comoara.gold
            comoara.colectat()
            comori.remove(comoara)
            setup_maze(levels[2])

    for inamic in inamiciii:
        if player.is_comoara(inamic):
            wn.clear()
            display_message("Game Over!YOU LOST!")


    wn.update()