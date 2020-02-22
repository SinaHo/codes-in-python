import smtplib
sender = "yohoo@yahoo.com"
receivers = ['sina.ho79@gmail.com']
message = """
Hello Test from me
"""
try:
    smtpObj = smtplib.SMTP('5.122.31.67)
    smtpObj.sendmail(sender, receivers, message)
    print("done")
except Exception as e:
     print(str(e))


