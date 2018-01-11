import library.json as json_loader
import library.mongodb as mongo
import library.file as file
import library.extract_cve_data as cve_data

# Load settings
settings_file = 'settings.json'
settings = json_loader.load_from_file(settings_file)
settings_mongo = settings['mongo_settings']

# Connect to MongoDB
mongo_client = mongo.connect_mongodb(settings_mongo['ip'], settings_mongo['port'])

# try to create a database and collection if it does not exist
db = mongo_client[settings['application_name']]
collection = db[settings['collection_name']]

count = 0

# Change Request : read from every JSON in the path and insert into MONGODB
for json_filepath in file.iterate_directory(settings['json_folder'], '.json'):
    # Read nvd CVE JSON file
    data = json_loader.load_from_file(json_filepath)

    # Iterate throughout the CVEs
    for cve in data['CVE_Items']:
        print("Reading {} data...".format(cve_data.Get_CVE_ID(cve)))
        # For each CVE, insert into MONGODB
        post_id = collection.insert_one(cve).inserted_id
        if post_id is not None:
            count += 1

print("Done... {} records added".format(count))