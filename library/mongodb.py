import pymongo

def connect_mongodb(ip, port):
    return pymongo.MongoClient(ip, int(port))