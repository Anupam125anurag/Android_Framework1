import smtplib
from library import base_lib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

device_name=base_lib.GET_DEVICE_NAME()
device_model=base_lib.GET_DEVICE_MODEL()
android_version=base_lib.GET_ANDROID_VERSION()
build_id=base_lib.GET_BUILD_ID()





msg = MIMEMultipart()
my_email="sushmas6998@gmail.com"
password="sushma123"
receiver_email="s.sushma6@tcs.com"
receiver2_email="anupam.anurag@tcs.com"
msg['From']=my_email
msg['To'] = receiver_email
subject_text= f"AUTOMATION OUTCOME: {device_model}"
msg['Subject'] = subject_text
body = f"Hello, Please find the report of Automation run on {device_name}." \
       f"Device Details:\nAndroid Version: {android_version} \nBuild ID: {build_id}\n Device Model: {device_model} \n\n\n\nThank You."

msg.attach(MIMEText(body, 'plain'))
filename="report.html"
attachment1 = open("/home/idm/Desktop/HDK855/report.html", "rb")
filename2="log.html"
attachment2 = open("/home/idm/Desktop/HDK855/log.html", "rb")


p = MIMEBase('application', 'octet-stream')
q = MIMEBase('application', 'octet-stream')
p.set_payload(attachment1.read())
encoders.encode_base64(p)
q.set_payload(attachment2.read())
encoders.encode_base64(q)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(p)
q.add_header('Content-Disposition', "attachment; filename= %s" % filename2)
msg.attach(q)


def set_connection(username,pswd):
    print("sending mail.....")
    connection=smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=username,password=pswd)
    text = msg.as_string()
    connection.sendmail(from_addr=username,to_addrs=receiver_email,msg=text)
    connection.sendmail(from_addr=username, to_addrs=receiver2_email, msg=text)
    connection.close()

    return "Done"


password="sushma123"

set_connection(my_email,password)

#connection.sendmail(from_addr=un, to_addrs="c.adithya@tcs.com",
                        #msg="Subject:Automation Report.\n\nHello, Please find the report of Automation run on Redmi Note 6 Pro. Device Details:\nAndroid Version: 9\nManufacturer: Xiaomi")

    #connection.sendmail(from_addr=un,to_addrs="archanakrishnamurthy55@gmail.com",msg="Hi",)
