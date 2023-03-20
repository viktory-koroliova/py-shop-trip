import json


class Shop:
    def __init__(self, shop_info: dict) -> None:
        self.name = shop_info["name"]
        self.location = shop_info["location"]
        self.products = shop_info["products"]


with open("config.json", "r") as file_in:
    shops_info = json.load(file_in)["shops"]

shop_list = []

for shop in shops_info:
    shop_list.append(Shop(shop))
