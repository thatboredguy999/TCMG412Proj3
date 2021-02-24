# This command will allow the file content from the url to run in python 
import urllib.request

urllib.request.urlretrieve("https://https://s3.amazonaws.com/tcmg476/http_access_log","data.txt")

# "t", "q1", "q2" are variables that will be executed for the overall outcome
t = open ('data.txt', 'r')
q1 = 0
q2 = 0

# The for loop will be iterating over the list of logs from the file and determining the number of logs documented
for line in t:
        if '/199' in line:
                q2 += 1
		
		if '/1995' in line:
			q1 += 1
			
# These print statements will give the outputs that were documented in the certain time periods
print 'The number of transactions documented in 1995 is' , q1
print 'The total number of transactions documented for this period is', q2
