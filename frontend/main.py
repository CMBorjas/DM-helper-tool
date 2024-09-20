import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import json

# Function to open a map image
def open_map():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg")])
    if file_path:
        load_map(file_path)

# Function to load the map on the canvas
def load_map(file_path):
    img = Image.open(file_path)
    img = img.resize((600, 400))  # Resize for display purposes
    img_tk = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor='nw', image=img_tk)
    canvas.image = img_tk  # Keep reference to prevent garbage collection
    draw_grid()  # Draw the grid overlay after loading the map

# Function to draw a grid overlay
def draw_grid():
    for i in range(0, 600, 40):  # Draw vertical lines
        canvas.create_line(i, 0, i, 400, fill="black")
    for j in range(0, 400, 40):  # Draw horizontal lines
        canvas.create_line(0, j, 600, j, fill="black")

# Function to create a new player token
def create_player_token(player_name, x, y):
    token = tk.Label(root, text=player_name, bg="blue", fg="white", width=10, height=2)
    token.place(x=x, y=y)
    token.bind("<B1-Motion>", lambda event, widget=token: on_drag(event, widget))

# Function to drag tokens
def on_drag(event, widget):
    widget.place(x=event.x_root - widget.winfo_width() // 2, y=event.y_root - widget.winfo_height() // 2)

# Save and load token positions
def save_positions():
    positions = []
    for token in tokens:
        positions.append({
            'name': token['text'],
            'x': token.winfo_x(),
            'y': token.winfo_y()
        })
    with open('player_positions.json', 'w') as f:
        json.dump(positions, f)

def load_positions():
    try:
        with open('player_positions.json', 'r') as f:
            positions = json.load(f)
            for position in positions:
                create_player_token(position['name'], position['x'], position['y'])
    except FileNotFoundError:
        pass

# Setup Tkinter window
root = tk.Tk()
root.title("Dungeon Master Map")
root.geometry("800x600")

# Canvas for the map
canvas = tk.Canvas(root, width=600, height=400, bg="gray")
canvas.pack(pady=20)

# Button to load a map
load_map_btn = tk.Button(root, text="Load Map", command=open_map)
load_map_btn.pack()

# Example of creating player tokens
create_player_token("Player 1", 50, 50)
create_player_token("Player 2", 150, 150)

root.mainloop()
