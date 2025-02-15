import tkinter as tk
from tkinter import font

class ParityGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("6x6 Data Grid with Parity Bits (Overall 7x7)")
        # Maximize window (works on Windows; adjust if necessary for other OS)
        self.root.state('zoomed')
        self.root.configure(bg="#e6f2ff")  # A soft blue background for the main window
        
        # Custom fonts
        self.title_font = font.Font(family="Helvetica", size=28, weight="bold")
        self.cell_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.parity_font = font.Font(family="Helvetica", size=16, weight="bold")
        
        # Create a title label
        title_label = tk.Label(self.root, text="Parity Checker", font=self.title_font, 
                               bg="#e6f2ff", fg="#003366", pady=10)
        title_label.pack()
        
        # Dimensions: data grid is 6x6; extra row/column for parity bits.
        self.data_rows = 6
        self.data_cols = 6
        
        # Create a 6x6 matrix for data cells initialized with 'w' (white)
        self.matrix = [['w' for _ in range(self.data_cols)] for _ in range(self.data_rows)]
        
        # Create a frame to hold the grid (data cells + parity bits)
        self.grid_frame = tk.Frame(self.root, bg="#e6f2ff")
        self.grid_frame.pack(expand=True)
        
        # Create buttons for the data grid (6x6)
        self.buttons = [[None for _ in range(self.data_cols)] for _ in range(self.data_rows)]
        for i in range(self.data_rows):
            for j in range(self.data_cols):
                btn = tk.Button(self.grid_frame, text=self.matrix[i][j],
                                width=4, height=2, font=self.cell_font,
                                bg="white", fg="black", relief="raised", bd=3,
                                command=lambda i=i, j=j: self.toggle_card(i, j))
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = btn
        
        # Create row parity labels (extra column at index data_cols) with light yellow background and red border
        self.row_parity_labels = []
        for i in range(self.data_rows):
            lbl = tk.Label(self.grid_frame, text="", width=6, height=2,
                           font=self.parity_font, bg="lightyellow", fg="black",
                           bd=3, relief="solid", highlightthickness=2, highlightbackground="red")
            lbl.grid(row=i, column=self.data_cols, padx=5, pady=5)
            self.row_parity_labels.append(lbl)
        
        # Create column parity labels (extra row at index data_rows) with light yellow background and red border
        self.col_parity_labels = []
        for j in range(self.data_cols):
            lbl = tk.Label(self.grid_frame, text="", width=4, height=2,
                           font=self.parity_font, bg="lightyellow", fg="black",
                           bd=3, relief="solid", highlightthickness=2, highlightbackground="red")
            lbl.grid(row=self.data_rows, column=j, padx=5, pady=5)
            self.col_parity_labels.append(lbl)
        
        # Bottom right cell (intersection of parity row and column) left blank
        self.blank_label = tk.Label(self.grid_frame, text="", width=6, height=2,
                                    font=self.parity_font, bg="#e6f2ff")
        self.blank_label.grid(row=self.data_rows, column=self.data_cols, padx=5, pady=5)
        
        # Update parity bits initially
        self.update_parity()
    
    def toggle_card(self, i, j):
        # Toggle the data cell at (i, j) between 'w' and 'b'
        self.matrix[i][j] = 'b' if self.matrix[i][j] == 'w' else 'w'
        self.buttons[i][j].config(
            text=self.matrix[i][j],
            bg="black" if self.matrix[i][j] == 'b' else "white",
            fg="white" if self.matrix[i][j] == 'b' else "black"
        )
        # Update parity bits after toggling
        self.update_parity()
    
    def update_parity(self):
        # Update row parity for each data row
        for i in range(self.data_rows):
            count_b = self.matrix[i].count('b')
            parity_text = "Even" if count_b % 2 == 0 else "Odd"
            self.row_parity_labels[i].config(text=parity_text)
        
        # Update column parity for each data column
        for j in range(self.data_cols):
            count_b = sum(1 for i in range(self.data_rows) if self.matrix[i][j] == 'b')
            parity_text = "Even" if count_b % 2 == 0 else "Odd"
            self.col_parity_labels[j].config(text=parity_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = ParityGUI(root)
    root.mainloop()
