import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import traceback
import os


def sendText(subject, msgTxt, phone_number, cell_carrier):
    try:
        carriers = {
            "AT&T": "@txt.att.net",
            "Sprint": "@messaging.sprintpcs.com",
            "T-Mobile": "@tmomail.net",
            "Verizon": "vtext.com",
            "Boost": "@myboostmobile.com",
            "Cricket": "@sms.mycricket.com",
            "Metro_PCS": "@mymetropcs.com",
            "Tracfone": "@mmst5.tracfone.com",
            "US_Cellular": "@email.uscc.net",
            "Virgin_Mobile": "@vmobl.com"
        }
        email = os.environ['SENDER_EMAIL']
        pas = os.environ["SENDER_PASSWORD"]

        sms_gateway = phone_number + carriers[cell_carrier]
        # The server we use to send emails in our case it will be gmail but every email provider has a different smtp 
        # and port is also provided by the email provider.
        smtp = "smtp.gmail.com" 
        port = 587
        # This will start our email server
        server = smtplib.SMTP(smtp,port)
        # Starting the server
        server.starttls()
        # Now we need to login
        server.login(email,pas)

        # Now we use the MIME module to structure our message.
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = sms_gateway
        # Make sure you add a new line in the subject
        msg['Subject'] = subject
        # Make sure you also add new lines to your body
        body = msgTxt
        # and then attach that body furthermore you can also send html content.
        msg.attach(MIMEText(body, 'plain'))

        sms = msg.as_string()

        server.sendmail(email,sms_gateway,sms)

        # lastly quit the server
        server.quit()
    except Exception as ex:
        traceback.print_exc()