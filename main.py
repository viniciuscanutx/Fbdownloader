from PySide2.QtWidgets import (QApplication, QMainWindow, QMessageBox)
from ui_main import Ui_MainWindow
import sys
import re
import requests
import urllib


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Feici Download")

        self.btndown.clicked.connect(self.fb_download)

    def fb_download(self):
        html = requests.get(self.txtlink.text())

        try:
            url = re.findall(r'hd_src:"(.*?)(?=",hd_tag)',
                             html.text, flags=re.I | re.S)
            urllib.request.urlretrieve(url[0], "Videos/fb_video.mp4")

        except:
            url = re.findall(r'sd_src:"(.*?)(?=",hd_tag)',
                             html.text, flags=re.I | re.S)
            urllib.request.urlretrieve(url[0], "Videos/fb_video.mp4")

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.SetWindowTitle("Download")
        msg.setText("Video Baixado!!")
        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
