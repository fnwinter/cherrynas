
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_URL = "smtp.gmail.com"
SMTP_PORT = 465

class EMail(object):
  sender_email = "fnwinter@gmail.com"
  receiver_email = "fnwinter@gmail.com"
  password = "" # app password
  title = ""
  text = ""
  html = ""

  def __init__(self, receiver = None):
    self.message = MIMEMultipart("alternative")
    self.message["Subject"] = self.title
    self.message["From"] = self.sender_email
    self.message["To"] = self.receiver_email
    if receiver:
      self.receiver_email = receiver

  def set_title(self, title):
    self.title = title

  def set_text(self, text):
    self.text = text

  def set_html(self, html):
    self.html = html

  def send_mail(self):
    part1, part2 = None, None
    if self.text:
      part1 = MIMEText(self.text, "plain")
      self.message.attach(part1)
    if self.html:
      part2 = MIMEText(self.html, "html")
      self.message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_URL, SMTP_PORT, context=context) as server:
        server.login(self.sender_email, self.password)
        server.sendmail(
            self.sender_email, self.receiver_email, self.message.as_string()
        )
        server.quit()