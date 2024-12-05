import tkinter as tk

class ChessGame:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Chess Game")
        self.board = [['R','N','B','Q','K','B','N','R'],
                      ['P','P','P','P','P','P','P','P'],
                      [' ',' ',' ',' ',' ',' ',' ',' '],
                      [' ',' ',' ',' ',' ',' ',' ',' '],
                      [' ',' ',' ',' ',' ',' ',' ',' '],
                      [' ',' ',' ',' ',' ',' ',' ',' '],
                      ['p','p','p','p','p','p','p','p'],
                      ['r','n','b','q','k','b','n','r']]
        self.current_player = 'white'
        self.selected_piece = None
        self.moves = []
        self.draw_board()
        
    def draw_board(self):
        self.canvas = tk.Canvas(self.parent, width=640, height=640)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.select_piece)
        for row in range(8):
            for col in range(8):
                color = 'white' if (row+col)%2 == 0 else 'grey'
                x1 = col*80
                y1 = row*80
                x2 = x1+80
                y2 = y1+80
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                piece = self.board[row][col]
                if piece != ' ':
                    filename = f"{piece}.png"
                    image = tk.PhotoImage(file=filename)
                    self.canvas.create_image(x1+40, y1+40, image=image)
                    self.canvas.image = image
        self.parent.mainloop()

    def select_piece(self, event):
        row = event.y//80
        col = event.x//80
        piece = self.board[row][col]
        if piece == ' ':
            return
        if self.selected_piece is None:
            if (self.current_player == 'white' and piece.isupper()) or \
               (self.current_player == 'black' and piece.islower()):
                self.selected_piece = (row, col)
        else:
            if self.selected_piece == (row, col):
                self.selected_piece = None
            else:
                move = (self.selected_piece, (row, col))
                if self.is_valid_move(move):
                    self.moves.append(move)
                    self.make_move(move)
                    self.current_player = 'white' if self.current_player == 'black' else 'black'
                self.selected_piece = None
        self.draw_board()
        
    def is_valid_move(self, move):
        # Check if the move is valid based on the game rules
        return True
        
    def make_move(self, move):
        # Update the board and pieces based on the move
        self.board[move[1][0]][move[1][1]] = self.board[move[0][0]][move[0][1]]
        self.board[move[0][0]][move[0][1]] = ' '
        
if __name__ == "__main__":
    root = tk.Tk()
    game = ChessGame(root)
 