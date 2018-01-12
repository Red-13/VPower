
# coding: utf-8

# In[49]:


###############################################################
# A simple retrieval of NIST Vul DB into local machine
# Auto unzip file if file extension is zip
# TODO: include more data feeds
# TODO: exception handling
###############################################################
import urllib.request
import zipfile

class UpdateVulDB:
    def download(self, file_url_path, file_name):
        urllib.request.urlretrieve(file_url_path, file_name)
        if "zip" in file_name:
            self.unzip(file_url_path, file_name)
    
    def unzip(self, file_url_path, file_name):
        zipfile.ZipFile(file_name).extractall()


# In[48]:


uvdb = UpdateVulDB()
uvdb.download("https://static.nvd.nist.gov/feeds/json/cve/1.0/nvdcve-1.0-2018.json.zip", "nvdcve-1.0-2018.json.zip")

