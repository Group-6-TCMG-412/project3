import os.path
import urllib.request

#file may already exist, setting path
path = './access.log'
check_file = os.path.isfile(path)

failures = 0
redirect = 0
success = 0
line_error = 0

with open("access.log",'r') as data_file:
        for line in data_file:
                data = line.split("\n")
                components = line.split(" ")
				
		if len(components) <= 4:
            line_error +=1
        
        else:

                userid = components[0]
                first_dash = components[1]
                second_dash = components[2]
                timestamp = components[3]
                timezone = components[4]
                request = components[5]
                resource_wanted = components[6]
                protocol = components[7]
                status = components[8]
                size = components[9]

                if status.startswith('4'):
                        failures +=1
                elif status.startswith('3'):
                        redirect +=1
                else:
                        success +=1

        print("# of line failures = " + str(line_error))
        print("# of failures = " + str(failures))
        print("# of redirects = " + str(redirect))
        print("# of successes = " + str(success))