import requests
import os

class Pokemon:
    def __init__(self,ja_name="",en_name="",weght=0.0,hight=0.0,flavor_text="",img=None):
        self.ja_name = ja_name
        self.en_name = en_name
        self.weght =weght
        self.hight = hight
        self.flavor_text = flavor_text
        self.img = img

def get_pokemon(id):
    pokemon = Pokemon()

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    pokeapi = response.json()

    species_url = pokeapi["species"]["url"]
    response = requests.get(species_url)
    pokeapi_species = response.json()

    pokemon.en_name = pokeapi["name"]
    pokemon.weght = float(pokeapi["weight"])/10
    pokemon.hight = float(pokeapi["height"])/10
    pokemon.img = pokeapi["sprites"]["other"]["official-artwork"]["front_default"]

    names = pokeapi_species["names"]
    for name in names:
        if name["language"]["name"] == "ja":
            pokemon.ja_name = name["name"]
            break

    flavor_text_entries = pokeapi_species["flavor_text_entries"]
    for text in flavor_text_entries:
        if text["language"]["name"] == "ja":
            pokemon.flavor_text = text["flavor_text"]

    download_img(pokemon)
    return pokemon

def download_img(pokemon:Pokemon):
    current_dir = os.path.dirname(__file__)
    img_path = f"{current_dir}/img/{pokemon.en_name}.png"
    if not os.path.isfile(img_path):
        image = requests.get(pokemon.img).content
        with open(img_path,"wb") as f:
            f.write(image)
    else:
        print("既にダウンロード済みのポケモン画像です")
    
    pokemon.img = img_path

print(get_pokemon(1).flavor_text)