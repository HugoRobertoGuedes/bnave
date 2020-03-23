from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

import os
import sys

# Dialog Window
class aboutWindow(QDialog):
    def __init__(self, *args, **kwargs):
        super(aboutWindow, self).__init__(*args, **kwargs)

        QBtn = QDialogButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("BNave")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        layout.addWidget(title)

        logo = QLabel()
        logo.setPixmap(QPixmap(os.path.join('images', 'ma-icon-128.png')))
        layout.addWidget(logo)

        layout.addWidget(QLabel("Version 1.0"))
        layout.addWidget(QLabel("Copyright 2020 H.G system."))

        for i in range(0, layout.count()):
            layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)

# Broswer Window
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Browser View
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://github.com/HugoRobertoGuedes"))
        self.setCentralWidget(self.browser)

        # Status Bar
        self.status = QStatusBar()
        self.setStatusBar(self.status)

        # listening events WebEngine
        self.browser.urlChanged.connect(self.updateStatus)
        self.browser.loadFinished.connect(self.titleWindowNav)

        # URL Toolbar
        urltb = QToolBar("Navigation Bar")
        urltb.setIconSize(QSize(16, 16))
        urltb.setMovable(False)

        # URL Toolbar : Actions

        # Home page
        homebtn = QAction(QIcon(os.path.join('icons', 'home.png')), "Home",self)
        homebtn.setStatusTip("Home page")
        homebtn.triggered.connect(self.toHome)

        # Back page
        backBtn = QAction(QIcon(os.path.join('icons', 'arrow-180.png')), "Back", self)
        backBtn.setStatusTip("Back to previous page")
        backBtn.triggered.connect(self.browser.back)

        # Forward page
        nextBtn = QAction(QIcon(os.path.join('icons', 'arrow.png')), "Forward", self)
        nextBtn.setStatusTip("Forward to next page")
        nextBtn.triggered.connect(self.browser.forward)

        # About
        aboutBtn = QAction(QIcon(os.path.join('icons', 'question.png')), "About", self)
        aboutBtn.setStatusTip("Open about window")
        aboutBtn.triggered.connect(self.about)

        # URL Edit
        self.urlBar = QLineEdit()
        self.urlBar.returnPressed.connect(self.navigate)

        # URL Toolbar add Actions
        urltb.addAction(homebtn)
        urltb.addAction(backBtn)
        urltb.addAction(nextBtn)
        urltb.addWidget(self.urlBar)
        urltb.addAction(aboutBtn)

        # Defaults options
        self.urlBar.setText('https://github.com/HugoRobertoGuedes')
        self.urlBar.setCursorPosition(0)
        self.showMaximized()

        # Menu and actions options
        self.addToolBar(urltb)

    # Functions

    # Navigate to URL
    def navigate(self):
        q = QUrl(self.urlBar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.browser.setUrl(q)

    # Update title this QmainWindow
    def titleWindowNav(self):
        title = self.browser.page().title()
        self.setWindowTitle("%s - BNave " % title)

    # Open the homepage
    def toHome(self):
        self.browser.setUrl(QUrl("https://github.com/HugoRobertoGuedes"))

    # Update status navigation
    def updateStatus(self, pagename):
        self.status.showMessage('Carregando ' + pagename.toString(), 2000)
    
    # Open dialog Window
    def about(self):
        dlg = aboutWindow()
        dlg.exec_()


# Start aplication
app = QApplication(sys.argv)
app.setApplicationName("BNave")
app.setOrganizationName("H.G System")
app.setOrganizationDomain("hgsystem.dev")
window = MainWindow()
window.show()
app.exec_()