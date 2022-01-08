from PyQt5.QtWidgets import *
from PyQt5 import uic

import smtplib
from email import encoders, message_from_string
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('main.ui', self)
        self.show()

        self.loginButton.clicked.connect(self.login)
        self.attachmentButton.clicked.connect(self.attach_sth)
        self.sendMail.clicked.connect(self.send_mail)

    def login(self):
        try:
            self.server = smtplib.SMTP(self.smtpInput.text(),self.portInput.text())
            self.server.ehlo()
            self.server.starttls()
            self.server.ehlo()
            self.server.login(self.emailInput.text(), self.passInput.text())

            self.smtpInput.setEnabled(False)
            self.portInput.setEnabled(False)
            self.emailInput.setEnabled(False)
            self.passInput.setEnabled(False)
            self.loginButton.setEnabled(False)

            self.to.setEnabled(True)
            self.attachmentButton.setEnabled(True)
            self.mailText.setEnabled(True)
            self.sendMail.setEnabled(True)
            self.subject.setEnabled(True)

            self.msg = MIMEMultipart()
        except smtplib.SMTPAuthenticationError:
            message_box = QMessageBox()
            message_box.setText("Invalid login info")
            message_box.exec()
        except:
            message_box = QMessageBox()
            message_box.setText("Login failed!")
            message_box.exec()

    def attach_sth(self):
        options = QFileDialog.Options()
        filenames, _ = QFileDialog.getOpenFileNames(self, "Select files", "", "All Files (*.*)", options=options)
        if filenames != []:
            for filename in filenames:
                attachment = open(filename, 'rb')

                filename = filename[filename.rfind("/")+1:]

                p = MIMEBase('aplication', 'octet-stream')
                p.set_payload(attachment.read())
                encoders.encode_base64(p)
                p.add_header('Content-Disposition', f"attachment; filename={filename}")                    
                self.msg.attach(p)
                if not self.attachments.text().endswith(':'):
                    self.attachments.setText(self.attachments.text() + ',')
                self.attachments.setText(self.attachments.text() + " " + filename)

    def send_mail(self):
        dialog = QMessageBox()
        dialog.setText("Do you want to send this mail?")
        dialog.addButton(QPushButton("Yes"), QMessageBox.YesRole)
        dialog.addButton(QPushButton("No"), QMessageBox.NoRole)

        if dialog.exec_() == 0:
            try:
                self.msg['From'] = self.emailInput.text()
                self.msg['To'] = self.to.text()
                self.msg['Subject'] = self.subject.text()
                self.msg.attach(MIMEText(self.mailText.toPlainText(), 'plain'))
                text = self.msg.as_string()
                self.server.sendmail(self.emailInput.text(), self.to.text(), text)
                message_box = QMessageBox()
                message_box.setText("Mail sent!")
                message_box.exec()
            except:
                message_box = QMessageBox()
                message_box.setText("Sending mail failed!")
                message_box.exec()

app = QApplication([])
window = MyGUI()
app.exec_()