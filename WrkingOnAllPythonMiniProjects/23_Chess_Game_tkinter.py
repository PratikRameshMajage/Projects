# import tkinter as tk

# class ChessGame:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Chess Game")
#         self.master.geometry("500x500")

# class ChessGame:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Chess Game")
#         self.master.geometry("500x500")
        
#         self.canvas = tk.Canvas(self.master, width=400, height=400)
#         self.canvas.pack()

# class ChessGame:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Chess Game")
#         self.master.geometry("500x500")
        
#         self.canvas = tk.Canvas(self.master, width=400, height=400)
#         self.canvas.pack()
        
#         for i in range(8):
#             for j in range(8):
#                 x1 = i * 50
#                 y1 = j * 50
#                 x2 = x1 + 50
#                 y2 = y1 + 50
#                 color = "white" if (i + j) % 2 == 0 else "gray"
#                 self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

# class ChessGame:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Chess Game")
#         self.master.geometry("500x500")
        
#         self.canvas = tk.Canvas(self.master, width=400, height=400)
#         self.canvas.pack()
        
#         self.pieces = {
#             "wr": tk.PhotoImage(file="pieces/wr.png"),
#             "wn": tk.PhotoImage(file="pieces/wn.png"),
#             "wb": tk.PhotoImage(file="pieces/wb.png"),
#             "wq": tk.PhotoImage(file="pieces/wq.png"),
#             "wk": tk.PhotoImage(file="pieces/wk.png"),
#             "wp": tk.PhotoImage(file="pieces/wp.png"),
#             "br": tk.PhotoImage(file="pieces/br.png"),
#             "bn": tk.PhotoImage(file="pieces/bn.png"),
#             "bb": tk.PhotoImage(file="pieces/bb.png"),
#             "bq": tk.PhotoImage(file="pieces/bq.png"),
#             "bk": tk.PhotoImage(file="pieces/bk.png"),
#             "bp": tk.PhotoImage(file="pieces/bp.png")
#         }
        
#         for i in range(8):    
#             for j in range(8):
#                 x1 = i * 50
#                 y1 = j * 50
#                 x2 = x1 + 50
#                 y2 = y1 + 50
#                 color = "white" if (i + j) % 2 == 0 else "gray"
#                 self.canvas.create_rectangle(x1, y1, x
