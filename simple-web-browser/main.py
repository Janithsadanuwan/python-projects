from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class MyWebBrowser():
    def __init__(self):
        self.window = QWidget()
        self.window.setWindowTitle("Simple Web Browser")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)

        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)

        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(30)

        self.forward_btn = QPushButton(">")
        self.forward_btn.setMinimumHeight(30)

        self.refresh_btn = QPushButton("Refresh")
        self.refresh_btn.setMinimumHeight(30)

        self.horizontal.addWidget(self.refresh_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)

        self.browser = QWebEngineView()

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(lambda: self.back())
        self.forward_btn.clicked.connect(lambda: self.forward())
        self.refresh_btn.clicked.connect(lambda: self.reload())

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("https://duckduckgo.com"))

        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self, url):
        if not url.startswith("http"):
            url = "https://duckduckgo.com/?q=" + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))

    def back(self):
        self.browser.back()
        self.url_bar.setText(self.browser.url().toString())
    
    def forward(self):
        self.browser.forward
        self.url_bar.setText(self.browser.url().toString())

    def reload(self):
        self.browser.reload()
        self.url_bar.setText(self.browser.url().toString())

app = QApplication([])
window = MyWebBrowser()
app.exec_()