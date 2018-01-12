
# coding: utf-8

# In[7]:


###############################################################
# A simple retrieval of CAPEC into local machine
# Auto unzip file if file extension is zip
# TODO: include more data feeds
# TODO: exception handling
###############################################################
import urllib.request
import zipfile
from xml.dom.minidom import parse
from json import dumps
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring

class UpdateVulDB:
    def download(self, file_url_path, file_name):
        urllib.request.urlretrieve(file_url_path, file_name)
        if "zip" in file_name:
            self.unzip(file_url_path, file_name)
    
    def unzip(self, file_url_path, file_name):
        zipfile.ZipFile(file_name).extractall()
        
    def convertXMLtoJSON(self, file_xml_path, file_json_path):
        dom1 = parse(file_xml_path)
        with open(file_json_path, "w") as text_file:
            text_file.write(dumps(bf.data(fromstring(dom1.toxml()))))


# In[8]:


#jupyter notebook --NotebookApp.iopub_data_rate_limit=1.0e10
uvdb = UpdateVulDB()
uvdb.download("http://capec.mitre.org/data/xml/capec_v2.11.xml", "capec_v2.11.xml")
uvdb.convertXMLtoJSON("C:\\Users\\win7\\capec_v2.11.xml", "C:\\Users\\win7\\capec_v2.11.json")
#uvdb.convertXMLtoJSON('<p id="main">Hello<b>bold</b></p>')

