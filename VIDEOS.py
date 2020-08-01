import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.browser = QtWebEngineWidgets.QWebEngineView()
        self.setCentralWidget(self.browser)

        self.tbNavigate = QtWidgets.QToolBar(orientation=QtCore.Qt.Horizontal)
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.tbNavigate)

        action_data = [
            ("Back", "icone/next.png", self.browser.back),
            ("Forward", "icone/next.png", self.browser.forward),
            (
                "Reload this page",
                "icone/baseline_refresh_black_18dp.png",
                self.browser.reload,
            ),
            ("Home", "icone/home (1).png", self.navigateHome),
        ]

        for text, icon_path, slot in action_data:
            icon = QtGui.QIcon()
            icon.addPixmap(
                QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off
            )
            action = QtWidgets.QAction(text, icon=icon, triggered=slot, parent=self)
            self.tbNavigate.addAction(action)

        self.httpsicon = QtWidgets.QLabel()
        self.tbNavigate.addWidget(self.httpsicon)

        self.addressbar = QtWidgets.QLineEdit()
        self.addressbar.returnPressed.connect(self.navigate_to_url)
        self.tbNavigate.addWidget(self.addressbar)
        self.browser.urlChanged.connect(self.update_urlBar)

        self.browser.load(QtCore.QUrl("https://youtube.com"))
        global_settings = QtWebEngineWidgets.QWebEngineSettings.globalSettings()

        for attr in (
            QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled,
            QtWebEngineWidgets.QWebEngineSettings.FullScreenSupportEnabled,
        ):
            global_settings.setAttribute(attr, True)
        self.browser.page().fullScreenRequested.connect(self.FullscreenRequest)

    @QtCore.pyqtSlot()
    def navigateHome(self):
        self.browser.setUrl(QtCore.QUrl("https://www.youtube.com"))

    @QtCore.pyqtSlot()
    def navigate_to_url(self):
        q = QtCore.QUrl(self.addressbar.text())
        if not q.scheme():
            q.setScheme("https")
        self.browser.setUrl(q)

    @QtCore.pyqtSlot(QtCore.QUrl)
    def update_urlBar(self, url):
        pixmap = (
            QtGui.QPixmap("icone/ssl.png")
            if url.scheme() == "https"
            else QtGui.QPixmap("icone/lock.png")
        )
        self.httpsicon.setPixmap(pixmap)
        self.addressbar.setText(url.toString())
        self.addressbar.setCursorPosition(0)

    @QtCore.pyqtSlot("QWebEngineFullScreenRequest")
    def FullscreenRequest(self, request):
        request.accept()
        if request.toggleOn():
            self.browser.setParent(None)
            self.browser.showFullScreen()
        else:
            self.setCentralWidget(self.browser)
            self.browser.showNormal()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
