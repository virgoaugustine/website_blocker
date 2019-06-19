from datetime import datetime as date
import time

path_to_hosts_file = 'ENTER PATH TO HOSTS FILE' 
# On Mac/Linux, it's /etc/hosts, and on Windows it's C:\Windows\System32\drivers\etc\hosts
redirect_URL = '127.0.0.1'
site_list = ['facebook.com','twitter.com'] #Type list of sites you want to block here.

while True:
    if date(date.now().year, date.now().month, date.now().day, 8) < date.now() < date(date.now().year, date.now().month, date.now().day, 17):
    #The values 8 and 17 above represent 8am and 5pm respectively. Change to suit the time you want to set the blocker to be active.
        print("Working Hours")

        with open(path_to_hosts_file,'r+') as file:
            content = file.read()
            
            for website in site_list:
                if website in content:
                    pass
                else:
                    file.write(redirect_URL + "\t " + website + "\n")
    
    else:
        print("Fun Hours")

        with open(path_to_hosts_file, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in site_list):
                    file.write(line)
            file.truncate()



    time.sleep(3)