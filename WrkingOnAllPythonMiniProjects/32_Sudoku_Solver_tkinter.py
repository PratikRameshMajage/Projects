import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Sudoku Solver")

# Create the 9x9 grid
grid = []
for i in range(9):
    row = []
    for j in range(9):
        cell = tk.Entry(window, width=3, font=("Arial", 16))
        cell.grid(row=i, column=j)
        row.append(cell)
    grid.append(row)

# Create the solve function
def solve():
    # Get the current state of the grid
    current_state = []
    for i in range(9):
        row = []
        for j in range(9):
            if grid[i][j].get() == "":
                row.append(0)
            else:
                row.append(int(grid[i][j].get()))
        current_state.append(row)

    # Define the helper function to check if the number is valid
    def is_valid(x, y, num):
        # Check row
        for i in range(9):
            if current_state[x][i] == num:
                return False
        # Check column
        for j in range(9):
            if current_state[j][y] == num:
                return False
        # Check 3x3 box
        box_x = (x // 3) * 3
        box_y = (y // 3) * 3
        for i in range(3):
            for j in range(3):
                if current_state[box_x+i][box_y+j] == num:
                    return False
        return True

    # Define the backtracking algorithm
    def backtrack():
        for i in range(9):
            for j in range(9):
                if current_state[i][j] == 0:
                    for num in range(1, 10):
                        if is_valid(i, j, num):
                            current_state[i][j] = num
                            if backtrack():
                                return True
                            current_state[i][j] = 0
                    return False
        return True

    # Run the backtracking algorithm
    backtrack()

    # Update the grid with the solution
    for i in range(9):
        for j in range(9):
            grid[i][j].delete(0, tk.END)
            grid[i][j].insert(0, str(current_state[i][j]))

# Create the solve button
solve_button = tk.Button(window, text="Solve", command=solve)
solve_button.grid(row=10, column=4)

# Start the GUI main loop
window.mainloop()
