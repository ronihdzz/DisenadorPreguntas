from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage, QWebEngineSettings
from PyQt5.QtWidgets import QApplication
import time
import sys




if __name__ == '__main__':
    app = QApplication(sys.argv)
    web = QWebEngineView()
    web.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
    web.page().fullScreenRequested.connect(lambda request: request.accept())
    baseUrl = "local"
    #LINK= https://youtu.be/TVsUhRnh2z0
    #ONLY=TVsUhRnh2z0
    # src="https://www.youtube.com/embed/AQUIINSERTEELLINK?rel=0&amp;showinfo=0"
    htmlString = """
            <iframe width="560" height="315" src="https://www.youtube.com/embed/TVsUhRnh2z0?rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>
             """
    web.setHtml(htmlString, QUrl(baseUrl))

    web.show()
    sys.exit(app.exec_())
