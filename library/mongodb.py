import pymongo
import library.extract_cve_data as cve_data

def connect_mongodb(ip, port):
    return pymongo.MongoClient(ip, int(port))

def upsert_mongodb(mongo_client, cve, db_name, collection_name):
    db = mongo_client[db_name]
    collection = db[collection_name]
    postid = collection.update_one({'cve.CVE_data_meta.ID' : cve_data.get_cve_id(cve)},
                                   {"$set":{"cve" : cve_data.get_cve(cve), "configurations" : cve_data.get_configurations(cve), "impact" : cve_data.get_impact(cve), "publishedDate": cve_data.get_published_date(cve), "lastModifiedDate": cve_data.get_last_modified_date(cve)}},
                                   upsert=True)
    return postid