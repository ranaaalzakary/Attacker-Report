import os
import time
import requests
import re
from collections import Counter
from geoip import geolite2


#To first start off with our script we need to clear the terminal to keep it clean
print("Hello Friend!, Welcome to the shortcut, the screen will be cleared in 2 seconds")
time.sleep(3)
os.system('clear')


with open('./syslog.log') as f_authlog:
	authlog = f_authlog.read()

	#Locates the IP addresses, tallys the number of occurrences, and stores the data in a dictionary
	ip_addresses = Counter(re.findall(r'authentication failure.*?rhost=([0-9.]*)\s', authlog))


	for i in range(0,11):

		#[0] is used to print the IP address once (it basically print the first element in the list which is the IP address)
		ip = list(ip_addresses.most_common()[i])[0]

		#This comprehensive list contains every instance when the IP has been reused, from which the true count can be determined. 
		cnt = list(ip_addresses.most_common()[i])[1]

		#Finding the physical location from which an IP address was assigned is what this does. 
		geo = geolite2.lookup(ip)
		if geo != None:
			print(f'''
{os.system('date')}
IP: {ip}
COUNT: {str(cnt)}
COUNTRY: {geo.country}
''') 
