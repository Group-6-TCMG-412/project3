import os.path
import urllib.request

#file may already exist, setting path
path = './access.log'
check_file = os.path.isfile(path)

#checking if access.log exists already, else downloading it
if check_file:
    print("File exists.")
else:
    print("Downloading log...")
    urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg476/http_access_log", "access.log")



with open("access.log",'r') as data_file:
        for line in data_file:
                data = line.split("\n")
                print(data)
                
        