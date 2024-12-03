import turtle
import random
import math
from time import sleep

# Set up the screen with background
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Animated Name")
screen.tracer(0)  # Turn off automatic updates for smooth animation

# Create lists to store different animation elements
stars = []
shooting_stars = []
glowing_effects = []

# Create stars in background
for _ in range(30):
    star = turtle.Turtle()
    star.hideturtle()
    star.penup()
    star.color("white")
    star.speed(0)
    x = random.randint(-380, 380)
    y = random.randint(-280, 280)
    star.goto(x, y)
    stars.append({"turtle": star, "twinkle_state": 0})

# Create shooting star class
class ShootingStar:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.color("white")
        self.reset_position()
        
    def reset_position(self):
        self.x = random.randint(-400, 400)
        self.y = 300
        self.speed = random.uniform(5, 15)
        self.angle = random.uniform(250, 290)
        
    def move(self):
        self.x += math.cos(math.radians(self.angle)) * self.speed
        self.y += math.sin(math.radians(self.angle)) * self.speed
        self.turtle.clear()
        self.turtle.goto(self.x, self.y)
        
        # Draw shooting star trail
        self.turtle.pendown()
        self.turtle.pensize(2)
        for i in range(4):
            self.turtle.forward(10)
            self.turtle.pensize(2 - i/2)
        self.turtle.penup()
        
        if self.y < -300:
            self.reset_position()

# Create shooting stars
for _ in range(3):
    shooting_stars.append(ShootingStar())

# Create main turtle for name
t = turtle.Turtle()
t.pensize(5)
t.speed(0)
t.hideturtle()

# Function to create glowing effect
def create_glow(x, y, color, size):
    glow = turtle.Turtle()
    glow.hideturtle()
    glow.penup()
    glow.goto(x, y)
    glow.color(color)
    glowing_effects.append({"turtle": glow, "size": size, "growing": True})

# Animation function
def animate():
    # Animate stars
    for star in stars:
        star["turtle"].clear()
        if star["twinkle_state"] == 0:
            star["turtle"].dot(random.randint(2, 4))
        else:
            star["turtle"].dot(random.randint(3, 6))
        star["twinkle_state"] = 1 - star["twinkle_state"]
    
    # Animate shooting stars
    for shooting_star in shooting_stars:
        shooting_star.move()
    
    # Animate glowing effects
    for effect in glowing_effects:
        effect["turtle"].clear()
        if effect["growing"]:
            effect["size"] += 0.2
            if effect["size"] > 20:
                effect["growing"] = False
        else:
            effect["size"] -= 0.2
            if effect["size"] < 10:
                effect["growing"] = True
        
        # Draw glow effect
        for i in range(3):
            effect["turtle"].dot(effect["size"] - i*3)
    
    screen.update()
    screen.ontimer(animate, 50)

# Draw name with effects
def draw_name():
    # Draw 'F'
    t.penup()
    t.goto(-350, 0)
    t.color("red")
    t.pendown()
    t.left(90)
    t.forward(100)
    create_glow(-350, 100, "red", 15)
    t.right(90)
    t.forward(60)
    t.backward(60)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(40)

    # Draw 'a'
    t.penup()
    t.goto(-250, 0)
    t.color("cyan")
    t.setheading(0)
    t.pendown()
    t.left(90)
    t.forward(60)
    create_glow(-250, 60, "cyan", 15)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(60)
    t.backward(30)
    t.left(90)
    t.forward(-40)

    # Draw 'i'
    t.penup()
    t.goto(-170, 0)
    t.color("lime")
    t.setheading(90)
    t.pendown()
    t.forward(60)
    create_glow(-170, 80, "lime", 15)
    t.penup()
    t.goto(-170, 80)
    t.pendown()
    t.dot(10)

    # Draw 'z'
    t.penup()
    t.goto(-90, 60)
    t.color("yellow")
    t.setheading(0)
    t.pendown()
    t.forward(40)
    create_glow(-90, 60, "yellow", 15)
    t.right(135)
    t.forward(85)
    t.left(135)
    t.forward(40)

    # Draw 'u'
    t.penup()
    t.goto(-10, 60)
    t.color("magenta")
    t.setheading(270)
    t.pendown()
    t.forward(60)
    create_glow(-10, 0, "magenta", 15)
    t.circle(20, 180)
    t.forward(60)

    # Draw 'l'
    t.penup()
    t.goto(70, 100)
    t.color("orange")
    t.setheading(270)
    t.pendown()
    t.forward(100)
    create_glow(70, 0, "orange", 15)

# Draw decorative stars
for _ in range(10):
    star = turtle.Turtle()
    star.hideturtle()
    star.penup()
    star.color("white")
    x = random.randint(-380, 380)
    y = random.randint(100, 280)
    star.goto(x, y)
    for _ in range(5):
        star.forward(10)
        star.right(144)

# Start the animation
draw_name()
animate()

# Keep the window open
screen.mainloop()
