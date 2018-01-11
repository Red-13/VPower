# Returns a list of vendors affected
def Get_Vendor_Name(cve):
    vendor_name_list = []
    for vendor_data in cve['cve']['affects']['vendor']['vendor_data']:
        vendor_name =  vendor_data['vendor_name']
        vendor_name_list.append(vendor_name)
    return vendor_name_list

def Get_Product(cve):
    product_list = []
    for vendor_data in cve['cve']['affects']['vendor']['vendor_data']:
        products_affected = vendor_data['product']['product_data']
        product_list.append(products_affected)
    return product_list

def Get_CVE_ID(cve):
    return cve['cve']['CVE_data_meta']['ID']

def Get_CVE_Description(cve):
    description_list = []
    for description_data in cve['cve']['description']:
        description_list.append(description_data)
    return description_list

def Get_Impact_v3(cve):
    baseMetricV3 = cve['impact']['baseMetricV3']
    cvssV3 = cve['impact']['baseMetricV3']['cvssV3']
    impact_dictionary = {
        "exploitabilityScore": baseMetricV3['exploitabilityScore'],
        "impactScore": baseMetricV3['impactScore'],
        "version" : cvssV3['version'],
        "attackVector": cvssV3['attackVector']
    }
    print(impact_dictionary)

