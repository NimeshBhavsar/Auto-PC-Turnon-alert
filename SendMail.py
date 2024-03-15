import time
import smtplib
import datetime
import socket
import os
from dotenv import load_dotenv
import requests
IPAddr=""
load_dotenv()
# Get the environment variable
password = os.getenv('PASSWORD')
emailid=os.getenv('EMAILID')
name=os.getenv('NAME')
# Now you can use the password variable in your code
hostname = socket.gethostname()
while(True):
    try:
        server = smtplib.SMTP('64.233.184.108',587)           #IP address of smtp.gmail.com to bypass DNS resolution
        def get_public_ip():
            response = requests.get('https://api.ipify.org')
            time.sleep(4)
            return response.text
        IPAddr = get_public_ip()
        break
    except:
        continue
server.starttls()
server.login(emailid,password)
timee=datetime.datetime.now()
stringg=""
stringg=stringg+"Your Computer Name is:" + hostname
stringg=stringg+"\nYour Computer IP Address is:" + IPAddr
body = "Dear "+name+","+"\n"+"\n"+"Your laptop has been accessed from a new location. If it was you, then you can ignore this email. \nTime: "+str(timee)+"\n"+stringg+"\n"+"\n"+"Regards,\nNimesh Bhavsar"
subject = "Computer has been accessed recently"
message = f'subject:{subject}\n\n{body}'
while(True):
    try:
        server.sendmail(emailid,emailid,message)
        break
    except:
        continue
server.quit()