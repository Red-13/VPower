import Library.Load_CVE_Data as Loader
import Library.Extract_CVE_Data as Extractor
import os

datafoldername = 'Datafile'
json_filename = 'nvdcve-1.0-2017.json'

json_filepath = os.path.join(os.sep,os.getcwd(),datafoldername,json_filename)

data = Loader.Load_JSON_From_File(json_filepath)

# Iterate throughout the CVEs
for cve in data['CVE_Items']:
    Extractor.Get_Impact_v3(cve)

    # Get the CVE ID
    print (Extractor.Get_CVE_ID(cve))



    # Get the vendor names to check
    for vendors_affected in Extractor.Get_Vendor_Name(cve):
        print(vendors_affected)

    # Get the products affected by each vendor
    for products_affected in Extractor.Get_Product(cve):
        print(products_affected)




