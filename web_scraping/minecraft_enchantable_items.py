import os
from pathlib import Path
from urllib.request import urlretrieve

from bs4 import BeautifulSoup as Soup

TMP = Path(os.getenv("TMP", "/tmp"))
HTML_FILE = TMP / "enchantment_list_pc.html"

# source:
# https://www.digminecraft.com/lists/enchantment_list_pc.php
URL = ("https://bites-data.s3.us-east-2.amazonaws.com/"
       "minecraft-enchantment.html")

possible_items = ["armor", "axe", "boots", "bow", "chestplate", "crossbow", "fishing_rod", "helmet", "pickaxe", "shovel",
             "sword", "trident"]


class Enchantment:
    """Minecraft enchantment class

    Implements the following:
        id_name, name, max_level, description, items
    """
    def __init__(self, id_name: str, name: str, max_level: int, description: str, items: [str]=None):
        if items is None:
            items = []
        self.id_name = id_name
        self.name = name
        self.max_level = max_level
        self.description = description
        self.items = items

    def __str__(self):
        return f"{self.name.title()} ({self.max_level}): {self.description}"


class Item:
    """Minecraft enchantable item class

    Implements the following:
        name, enchantments
    """
    def __init__(self, name: str, enchantments: [Enchantment]=None):
        if enchantments is None:
            enchantments = []
        self.name = name
        self.enchantments = enchantments

    def __str__(self):
        return_str = f"{self.name.replace('_', ' ').title()}: \n"
        for enchantment in sorted(self.enchantments, key=lambda ench: ench.id_name):
            return_str += f"  [{enchantment.max_level}] {enchantment.id_name}\n"
        return return_str


def generate_enchantments(soup):
    """Generates a dictionary of Enchantment objects

    With the key being the id_name of the enchantment.
    """
    table = soup.find("table",{"class":"std_table"})
    rows = table.find_all("tr")
    enchantment_dict = {}
    for row in rows:
        tds = row.find_all("td")
        if tds and len(tds) == 6:
            id_name = ""
            for content in tds[0].find("em").contents:
                if isinstance(content, str):
                    id_name += content
            name = tds[0].find("a").text
            max_level = num_roman_to_arabic(tds[1].text)
            description = tds[2].text
            items = item_names_from_str(tds[4].next.attrs["data-src"])
            enchantment_dict[id_name] = Enchantment(id_name, name, max_level, description, items)
    return enchantment_dict


def generate_items(data):
    """Generates a dictionary of Item objects

    With the key being the item name.
    """
    minecraft_items_dict = {}
    for item_name in possible_items:
        item = Item(item_name)
        for enchantment in data.values():
            if item_name in enchantment.items:
                item.enchantments.append(enchantment)
        minecraft_items_dict[item_name] = item
    return minecraft_items_dict


def get_soup(file=HTML_FILE):
    """Retrieves/takes source HTML and returns a BeautifulSoup object"""
    if isinstance(file, Path):
        if not file.is_file():
            urlretrieve(URL, file)

        with file.open() as html_source:
            soup = Soup(html_source, "html.parser")
    else:
        soup = Soup(file, "html.parser")

    return soup


def num_roman_to_arabic(roman: str) -> int:
    match roman:
        case "I":
            return 1
        case "II":
            return 2
        case "III":
            return 3
        case "IV":
            return 4
        case "V":
            return 5
        case _:
            return 0


def item_names_from_str(item_str: str) -> [str]:
    item_str = item_str.split('/')[-1].split('.')[0].replace("fishing_rod", "fishing rod")
    item_str = item_str.replace('_', '|')
    names = item_str.replace("fishing rod", "fishing_rod").split('|')
    return [name for name in names if name in possible_items]


def main():
    """This function is here to help you test your final code.

    Once complete, the print out should match what's at the bottom of this file"""
    soup = get_soup()
    enchantment_data = generate_enchantments(soup)
    minecraft_items = generate_items(enchantment_data)
    for item in minecraft_items:
        print(minecraft_items[item], "\n")


if __name__ == "__main__":
    main()

"""
Armor: 
  [1] binding_curse
  [4] blast_protection
  [4] fire_protection
  [4] projectile_protection
  [4] protection
  [3] thorns 

Axe: 
  [5] bane_of_arthropods
  [5] efficiency
  [3] fortune
  [5] sharpness
  [1] silk_touch
  [5] smite 

Boots: 
  [3] depth_strider
  [4] feather_falling
  [2] frost_walker 

Bow: 
  [1] flame
  [1] infinity
  [5] power
  [2] punch 

Chestplate: 
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Crossbow: 
  [1] multishot
  [4] piercing
  [3] quick_charge 

Fishing Rod: 
  [3] luck_of_the_sea
  [3] lure
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Helmet: 
  [1] aqua_affinity
  [3] respiration 

Pickaxe: 
  [5] efficiency
  [3] fortune
  [1] mending
  [1] silk_touch
  [3] unbreaking
  [1] vanishing_curse 

Shovel: 
  [5] efficiency
  [3] fortune
  [1] silk_touch 

Sword: 
  [5] bane_of_arthropods
  [2] fire_aspect
  [2] knockback
  [3] looting
  [1] mending
  [5] sharpness
  [5] smite
  [3] sweeping
  [3] unbreaking
  [1] vanishing_curse 

Trident: 
  [1] channeling
  [5] impaling
  [3] loyalty
  [3] riptide
"""