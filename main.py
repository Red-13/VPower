import library.json as json_loader
import library.file as file
import library.mongodb as mongo
import library.extract_cve_data as cve_data
import downloader.nvd.download as downloader

# Load settings
settings_file = 'settings.json'
settings = json_loader.load_from_file(settings_file)
settings_mongo = settings['mongo_settings']

# If there is a need to download files, set 'true' in settings.json
if(settings['download_files']):
    # Load List of targets to download
    download_urls = 'download_urls.json'
    urls = json_loader.load_from_file(download_urls)

    # Download all the JSON files first
    downloader.download_definitions(settings['json_folder'], urls)

# Connect to MongoDB
mongo_client = mongo.connect_mongodb(settings_mongo['ip'], settings_mongo['port'])
print("Connected to MongoDB at {}".format(settings_mongo['ip']))

# Read from every JSON in the path and insert into MONGODB
count = 0
for json_filepath in file.iterate_directory(settings['json_folder'], '.json'):
    # Read nvd CVE JSON file
    data = json_loader.load_from_file(json_filepath)
    print("Loaded JSON data from {}".format(json_filepath))

    # Iterate throughout the CVEs
    for cve in data['CVE_Items']:
        cve_id = cve_data.get_cve_id(cve)

        # For each CVE, insert into MONGODB
        post_id = mongo.upsert_mongodb(mongo_client, cve, settings['application_name'], settings['collection_name'])
        if post_id is not None:
            print("Adding data {}".format(cve_id))
            count += 1
print("Done... {} records added".format(count))