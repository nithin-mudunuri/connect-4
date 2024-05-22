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
            squares = Rectangle(Point(x - 75, y - 75), Point(x + 75, y + 75))
            squares.setFill("blue")
            squares.draw(win)
            circle = Circle(Point(x, y), 50)
            circle.setFill("dark gray")
            circle.draw(win)


    # Draw 6 rows of circles and 7 columns
    rows, cols = 6, 7
    y_positions = [100, 250, 400, 550, 700, 850]
    grid = [["" for _ in range(cols)] for _ in range(rows)]
    for y in y_positions:
        draw_row(y)
    counters = [6, 6, 6, 6, 6, 6, 6]

    def set_gravity(x):
        columns = [50, 200, 350, 500, 650, 800, 950]

        for i in range(len(columns)):
            if x < columns[i] + 50:  # Each circle's center is at + 50
                if counters[i] == -1:
                    break
                counters[i] -= 1
                break
    def place_token(x):
        columns = [50, 200, 350, 500, 650, 800, 950]
        for col in range(len(columns)):
            if x < columns[col] + 50 and counters[col] > 0:
                row = counters[col] - 1
                grid[row][col] = current_color
                circle = Circle(Point(columns[col], y_positions[row]), 50)
                circle.setFill(current_color)
                circle.draw(win)
                counters[col] -= 1
                return row, col
        return None, None

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

    def check_winner(row, col, color):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

        for dr, dc in directions:
            count = 1  # Start with the current token
            for i in range(1, 4):
                r, c = row + dr * i, col + dc * i
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == color:
                    count += 1
                else:
                    break
            for i in range(1, 4):
                r, c = row - dr * i, col - dc * i
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == color:
                    count += 1
                else:
                    break
            if count >= 4:
                return True
        return False

    while True:
        click_point = win.getMouse()
        x = click_point.getX()
        row, col = place_token(x)
        if row is not None and col is not None:
            if check_winner(row, col, current_color):
                print(f"Player with color {current_color} wins!")
                z.setText(f"{current_color.capitalize()} Wins!")
                z.setFill(current_color)
                break
            change_color()



main()