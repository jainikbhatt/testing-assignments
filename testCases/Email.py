import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header

fromaddr = "Jainik Bhatt <jainikjbhatt@gmail.com>"
toaddr = 'Jainik Bhatt <jainikjbhatt@gmail.com>', 'Nehal Dave <nehaldave4646@gmail.com>'

# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = fromaddr

# storing the receivers email address
msg['To'] = Header(','.join(toaddr))

# storing the subject
msg['Subject'] = "Automation Testing Report"

# string to store the body of the mail
body = "Hello Team, kindly find attached html report"

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
filename = "Report.html"
attachment = open("C://Users//Shree//PycharmProjects//Project//pythonProject//pythonProject//RTI_Test_Project//Reports//report.html", "rb")

# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload(attachment.read())

# encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
msg.attach(p)

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("jainikjbhatt@gmail.com", "kzfravxmuhdccmxw")

# Converts the Multipart msg into a string
text = msg.as_string()

# sending the mail
s.sendmail(fromaddr, toaddr, text)

# terminating the session
s.quit()
