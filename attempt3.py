import os.path
import urllib.request

path = './access.log'
check_file = os.path.isfile(path)

past6months = 0
alltime = 0

if check_file = "False":
    print("Downloading log...")
    urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg476/http_access_log", "access.log")
	
else:
	with open("access.log",'r') as data_file:
			for line in data_file:
					data = line.split("\n")

			pieces = line.split(" ")
			if len(pieces) >=11:
					identity = pieces[0]
					time = pieces[1]
					request_type = pieces[2]
					response = pieces[3]
					object_size = pieces[4]
					alltime += 1

					timestamp = time[1:]
					date = datetime.strptime(date_str, "%d/%b/%Y:%H:%M:%S").date()

					if date > datetime(1995, 6, 1).date() and date <= datetime(1995, 12, 1).date():
							past6months += 1

print("Total Requests:", alltime)
print("Total Requests in 6 Months:", past6months)