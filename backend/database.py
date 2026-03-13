from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["packet_sniffer"]

packets_collection = db["packets"]