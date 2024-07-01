import tkinter as tk
import random

destinations = [
    "Santorini, Greece - Sunset by the sea",
    "Kyoto, Japan - Explore ancient temples",
    "Machu Picchu, Peru - Hike the Andes",
    "Reykjavik, Iceland - See the Northern Lights",
    "Cape Town, South Africa - Safari adventure",
    "Queenstown, New Zealand - Bungee jump",
    "Bora Bora, French Polynesia - Overwater bungalows",
    "Cusco, Peru - Visit the Sacred Valley",
    "Petra, Jordan - Discover the ancient city",
    "woo woo, hazaribagh - to visit a lands of thousands of garden",
    "wakka wakka, africa - for visiting new species",
    "Banff, Canada - Rocky Mountains retreat"
]

def get_random_destination():
    destination = random.choice(destinations)
    destination_label.config(text=destination)

root = tk.Tk()
root.title("Random Teleportation App")

destination_label = tk.Label(root, text="Where will you go next?", font=("Helvetica", 20), wraplength=400)
destination_label.pack(pady=20)

teleport_button = tk.Button(root, text="Teleport Me!", font=("Helvetica", 18), command=get_random_destination)
teleport_button.pack(pady=20)

root.mainloop()
