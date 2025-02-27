import pymongo
import  certifi

connection_string = "mongodb+srv://BigBlue60:Naybor60$@fsdi-107.itfhn.mongodb.net/?retryWrites=true&w=majority&appName=fsdi-107"

client = pymongo.MongoClient(connection_string, tlsCAFile=certifi.where())
db = client.get_database('LifeGoods')
