from Shop import *

class Company:
    def __init__(self, name):
        self.name = name
        self.dict_shops = []

    def get_name(self):
        return self.name

    def get_count_shops(self):
        return len(self.dict_shops)

    def get_shop_names(self):
        shops = []
        for shop in self.dict_shops:
            shops.append(shop.get_id())
        return shops

    def get_shop(self, _id):
        i = 0
        print(type(_id))
        for shop in self.dict_shops:
            if (shop.get_id() == _id):
                return shop
            i += 1
        return -1
    
    def add_shop(self):
        new_id = len(self.dict_shops)
        new_shop = Shop(new_id)
        self.dict_shops.append(new_shop)
        return new_id
