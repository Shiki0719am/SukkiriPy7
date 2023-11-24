import tkinter as tk
import pokeapi

def key(e):
    print(e.keysym)
def mouse(e):
    print(e.x)
def change_data(entry_id):
    pokemon = pokeapi.get_pokemon(entry_id)
    name_label["text"] = pokemon.ja_name
    data_label["text"] = f"高さ:{pokemon.hight}m,重さ:{pokemon.weght}kg"
    img["file"] = pokemon.img
    flavor_text_msg["text"] = pokemon.flavor_text

if __name__ == "__main__":
    font_size = 20
    pokemon =pokeapi.get_pokemon(1)

    root = tk.Tk()
    root.geometry("1280x720")

    entry_frame = tk.Frame(root)
    pokemon_frame = tk.Frame(root)
    entry_frame.pack()
    pokemon_frame.pack()

    entry_label = tk.Label(entry_frame,text="図鑑番号:", font=font_size)
    entry_id = tk.Entry(entry_frame,font=font_size)
    entry_button = tk.Button(entry_frame,text="検索",command=lambda:change_data(entry_id.get()))

    entry_label.grid(row=0,column=0)
    entry_id.grid(row=0,column=1)
    entry_button.grid(row=0,column=2)

    name_label = tk.Label(pokemon_frame,text=pokemon.ja_name,font=font_size)
    img = tk.PhotoImage(file=pokemon.img)
    image_label = tk.Label(pokemon_frame,image=img)
    data_label = tk.Label(
        pokemon_frame,
        text=f"高さ:{pokemon.hight}m,重さ:{pokemon.weght}kg",
        font=font_size
    )
    flavor_text_msg = tk.Message(
        pokemon_frame,
        text=pokemon.flavor_text,
        font=font_size,
        width=400
    )

    name_label.pack()
    image_label.pack()
    data_label.pack()
    flavor_text_msg.pack(pady=(10,0))

    root.bind("<Key>",key)
    root.bind("<Button-1>",mouse)
    root.bind("<KeyRelease>",mouse)
    root.bind("<Motion>",mouse)
    root.mainloop()