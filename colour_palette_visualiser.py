import tkinter as tk
root = tk.Tk()
root.config(bg="#ffffff")
root.resizable(width=False, height=False)
root.title("Elecarno's Colour Palette Visualiser [ASTER]")

# colours
colour_1 = "#999999"
colour_2 = "#666666"
colour_3 = "#333333"

# define canvas
canvas = tk.Canvas(root, height=200, width=1000, bg="#ffffff", bd=0)
canvas.pack()

# ---------------------------------------------define colour panels row 1-----------------------------------------------
# define colour panel 1
col_panel_1 = tk.Label(bg=colour_1)
col_panel_1.place(x=0, y=0, height=100, width=100,)
col_panel_1_hex = tk.Label(bg=colour_1, text=colour_1 + "\nprimary", fg="#ffffff")
col_panel_1_hex.place(x=0, y=0, height=40, width=100)

# define colour panel 2
col_panel_2 = tk.Label(bg=colour_2)
col_panel_2.place(x=100, y=0, height=100, width=100,)
col_panel_2_hex = tk.Label(bg=colour_2, text=colour_2 + "\nsecondary", fg="#ffffff")
col_panel_2_hex.place(x=100, y=0, height=40, width=100)

# define colour panel 3
col_panel_3 = tk.Label(bg=colour_3)
col_panel_3.place(x=200, y=0, height=100, width=100,)
col_panel_3_hex = tk.Label(bg=colour_3, text=colour_3 + "\ntertiary", fg="#ffffff")
col_panel_3_hex.place(x=200, y=0, height=40, width=100)

root.mainloop()
