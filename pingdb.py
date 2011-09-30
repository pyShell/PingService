import pymongo


class DatabaseHandler():
    def __init__(self):
        self.pings = pymongo.Connection('localhost').ping_db.pings
    
    def insert_value(self, ping_time, time):
        self.pings.insert({'ping_time': ping_time, 'time': time})
        
    def get_values(self):
        return self.pings.find()
        
        