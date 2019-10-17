from pymongo import MongoClient
from bson.objectid import ObjectId

restroom_1 = {
    'restroom_name': 'Make School',
    'restroom_gender' : 'All Gender Restroom',
    'pic_path' : '/static/makeschool.jpeg',
    'restroom_price' : 'FREE'
}

restroom_2 = {
    'restroom_name': 'Starbucks',
    'restroom_gender' : 'All Gender Restroom',
    'pic_path' : '/static/starbucks.jpeg',
    'restroom_price' : "FREE"
}

restroom_3 = {
    'restroom_name': 'Captial One Cafe',
    'restroom_gender' : 'All Gender Restroom',
    'pic_path' : '/static/captial_one.jpeg',
    'restroom_price' : "FREE"
}

restroom_4 = {
    'restroom_name': 'Nespresso',
    'restroom_gender': 'All Gender Restroom',
    'pic_path' : '/static/nespresso.jpeg',
    'restroom_price' : "FREE"
}

restroom_5 = {
    'restroom_name': 'Little Delhi ',
    'restroom_gender': 'All Gender Restroom',
    'pic_path' : '/static/little_delhi.jpg',
    'restroom_price' : "FREE"
}

inventory_list = [
    restroom_1,
    restroom_2,
    restroom_3,
    restroom_4,
    restroom_5
]

class Restrooms():
    def __init__(self, inventory):
        self.inventory = inventory
    
    def show_inventory(self):
        self.inventory.delete_many({})
        
        self.inventory.insert_many(inventory_list)
        
        for i in self.inventory.find():
            print(inventory_list)