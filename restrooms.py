from pymongo import MongoClient
from bson.objectid import ObjectId

restroom_1 = {
    'restroom_name': 'Make School',
    'restroom_gender' : 'All Gender Restroom',
    'pic_path' : '/static/makeschool.jpeg',
    'restroom_price' : 'FREE',
    'google_map': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3153.0996137917773!2d-122.41312704960261!3d37.787705219089986!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8085807f8bd4d441%3A0xd4618e6f27febe26!2sMake%20School!5e0!3m2!1sen!2sus!4v1571348027959!5m2!1sen!2sus"
}

restroom_2 = {
    'restroom_name': 'Starbucks',
    'restroom_gender' : 'All Gender Restroom',
    'pic_path' : '/static/starbucks.jpeg',
    'restroom_price' : "FREE",
    'google_map': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1576.5627415026152!2d-122.41148017228738!3d37.78709892790962!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x20cd7876b1d66114!2sStarbucks!5e0!3m2!1sen!2sus!4v1571348747807!5m2!1sen!2sus"
}

restroom_3 = {
    'restroom_name': 'Captial One Cafe',
    'restroom_gender' : 'All Gender Restroom',
    'pic_path' : '/static/captial_one.jpeg',
    'restroom_price' : "FREE",
    'google_map': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3153.0560489997624!2d-122.40611104960239!3d37.78872621903128!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80858088534e8e41%3A0xccfca40eb1e75ed1!2sCapital%20One%20Caf%C3%A9!5e0!3m2!1sen!2sus!4v1571348807561!5m2!1sen!2sus"
}

restroom_4 = {
    'restroom_name': 'Nespresso',
    'restroom_gender': 'All Gender Restroom',
    'pic_path' : '/static/nespresso.jpeg',
    'restroom_price' : "FREE",
    'google_map': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d12612.220637161836!2d-122.41270395890429!3d37.788747070330075!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x32ce7e7216b98420!2sNespresso%20Boutique!5e0!3m2!1sen!2sus!4v1571348865689!5m2!1sen!2sus"
}

restroom_5 = {
    'restroom_name': 'Little Delhi ',
    'restroom_gender': 'All Gender Restroom',
    'pic_path' : '/static/little_delhi.jpg',
    'restroom_price' : "NOT FREE",
    'google_map': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3153.2457512081683!2d-122.41134804960257!3d37.78428011928715!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x808580858fb0dd73%3A0xb45574ee76558eec!2sLittle%20Delhi!5e0!3m2!1sen!2sus!4v1571348909046!5m2!1sen!2sus"
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