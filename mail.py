import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import xlrd


def mail(name):

    wb = xlrd.open_workbook('pass.xlsx')
    ws1 = wb.sheet_by_index(0)
    password = ws1.cell_value(0,1)

    email_user = ws1.cell_value(0,0)
    email_send = ws1.cell_value(0,0)

    subject = 'subject'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = 'detected some motion'
    msg.attach(MIMEText(body,'plain'))

    filename='./images/{}'.format(name)
    attachment  =open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()


    server = smtplib.SMTP('smtp.gmail.com',587)

    server.starttls()

    server.login(email_user,password)


    server.sendmail(email_user,email_send,text)
    server.quit()
