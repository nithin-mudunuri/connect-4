from graphics import *
def main():
    win = GraphWin("My Circle", 1000, 1000)
    r = Rectangle(Point(0,0), Point(1000,1000))
    r.setFill("black")
    r.draw(win)
    current_color = "red"
    red = 0
    yellow = 0
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
    counters = [5, 5, 5, 5, 5, 5, 5]

    def set_gravity(x):
        columns = [100, 250, 400, 550, 700, 850]

        for i in range(len(columns)):
            if x < columns[i] + 50:  # Each circle's center is at + 50
                counters[i] -= 1
                break
    def place_token(x):
        columns = [50, 200, 350, 500, 650, 800, 950]
        global red
        global yellow
        for i in range(len(columns)):
            if x < columns[i] + 50:  # Each circle's center is at + 50
                circle = Circle(Point(columns[i], counters[i]), 50)
                circle.setFill(current_color)
                if(current_color == "red"):
                    red += 1
                if (current_color == "yellow"):
                    yellow += 1
                circle.draw(win)
                break


    while True:
        click_point = win.getMouse()
        xs = click_point.getX()  # Get the x-coordinate of the click
        set_gravity(xs)
        place_token(xs)

main()