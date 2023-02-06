import os.path
import urllib.request    

path = './access.log'
check_file = os.path.isfile(path)

if check_file = true:
    print("File exists.")
else:
    print("Downloading log.")
    urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg476/http_access_log", "access.log")