from pymongo import MongoClient
import datetime
from time import sleep



date = datetime.date.today()
new_collec = f'exitpnl_{date}'

try:
    client = MongoClient()
    db = client['Cumulative_symphonyorder']
    collec = f'cumulative_{date}'
    db.create_collection(collec)
    print(f"created new collection '{collec}'")

except Exception as e:
    print(e)

try:
    new_client = MongoClient()
    exitpnl_db = new_client['exitpnl']
    exitpnl_db[new_collec].drop()
    print('exitpnl Collec Deleted')
except:
    pass

try:
    new_client = MongoClient()
    new_db = new_client['exitpnl']
    new_db.create_collection(new_collec)
    print(f"created new collection '{new_collec}'")

except Exception as e:
    print(e)


# algoname_unique = db[collec].find().distinct("algoName")
# print(algoname_unique)

# ClientID_unique = db[collec].find().distinct("clientID")
# print(ClientID_unique)

# l = []
# for x in algoname_unique:
#     for y in ClientID_unique:
#         conca = x + y
#         l.append(conca)       
# print(l)    

while True:
    check = db[collec].find()
    li = []

    for z in check:    
        conca = z["clientID"]+ z["algoName"]
        if conca in li:
            continue
           
        else:
            li.append(conca)
            match = new_db[new_collec].find_one({ "$and" : [{"algoName": z['algoName']},{"clientID": z['clientID']}] })
            if match:
                try:
                    new_db[new_collec].update({'_id' : match['_id']}, {"$set": {"strategywise_pnl": z['strategywise_pnl']}})
                except Exception:
                    print("Waiting for PnL")
                    pass

            else:
                try:
                    post={"algoName":z['algoName'], "clientID":z['clientID'],"strategywise_pnl":z['strategywise_pnl']}
                    new_db[new_collec].insert_one(post)
                except Exception:
                    print("Waiting for PnL")
                    pass

        
        
        
        
        
        
          # check = db[collec].find()
                    # l = []
                    # for x in check:    
                    #     conca = x["clientID"]+ x["algoName"]
                    #     if conca in l:
                    #         continue
                    #     else:
                    #         l.append(conca)
                    #         new_db[new_collec].insert(db[collec].find({},{ "_id": 0, "algoName": 1, "clientID": 1, "strategywise_pnl": 1 }))
