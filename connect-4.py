from graphics import *
def main():
    win = GraphWin("My Circle", 1000, 1000)
    r = Rectangle(Point(0,0), Point(1000,1000))
    r.setFill("black")
    r.draw(win)
    z = Text(Point(500,950), "Red's Turn")
    z.setSize(30)
    z.setFill("red")
    z.draw(win)
    current_color = "red"

    def draw_row(y):
        for i in range(7):
            x = 50 + i * 150
            circle = Circle(Point(x, y), 50)
            circle.setFill("gray")
            circle.draw(win)

    # Draw 6 rows of circles
    y_positions = [100, 250, 400, 550, 700, 850]
    for y in y_positions:
        draw_row(y)
    counters = [6, 6, 6, 6, 6, 6, 6]

    def set_gravity(x):
        columns = [50, 200, 350, 500, 650, 800, 950]

        for i in range(len(columns)):
            if x < columns[i] + 50:  # Each circle's center is at + 50
                if(counters[i] == -1):
                    break
                counters[i] -= 1
                break
    def place_token(x):
        columns = [50, 200, 350, 500, 650, 800, 950]
        for i in range(len(columns)):
            if x < columns[i] + 50:  # Each circle's center is at + 50
                if counters[i] == -1:
                    break
                circle = Circle(Point(columns[i], y_positions[counters[i]]), 50)
                circle.setFill(current_color)
                circle.draw(win)
                change_color()
                break

    def change_color():
        nonlocal current_color
        nonlocal z
        if current_color == "red":
            current_color = "yellow"
            z.undraw()
            z = Text(Point(500, 950), "Yellow's Turn")
            z.setSize(30)
            z.setFill("yellow")
            z.draw(win)

        else:
            current_color = "red"
            z.undraw()
            z = Text(Point(500, 950), "Red's Turn")
            z.setSize(30)
            z.setFill("red")
            z.draw(win)

    while True:
        click_point = win.getMouse()
        xs = click_point.getX()  # Get the x-coordinate of the click
        set_gravity(xs)
        place_token(xs)



main()