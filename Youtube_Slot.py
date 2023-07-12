import time


from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from SON6 import Ui_MainWindow
from PyQt5.QtCore import pyqtSlot, pyqtSignal,QCoreApplication,QProcess,QRect
import yt_dlp  #Video indirme kütüphanesi
import os
import icons_rc


class dersler_7(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.push_indirilenler.clicked.connect(self.indirilenleri_Ac)
        self.ui.push_indir.clicked.connect(self.butona_bas) #Butona basıldığında ekrana hello yazan signal slot bağlantısı.
        self.ui.push_yenile.clicked.connect(self.yeniden_baslat)
        self.ui.push_kapat.clicked.connect(self.kapat)


    def yeniden_baslat(self):
        try:
            self.ui.label_linkbekleniyor2.setText(QCoreApplication.translate("MainWindow","<html><head/><body><p align=\"center\"><span style=\" font-size:7pt; font-weight:600; color:#dfd2d3;\">LİNK BEKLENİYOR..</span></p></body></html>"))
            self.ui.label_linkbekleniyor1.setText(QCoreApplication.translate("MainWindow","<html><head/><body><p align=\"center\"><span style=\" font-size:7pt; font-weight:600; color:#dfd2d3;\">LİNK BEKLENİYOR..</span></p></body></html>"))
            QApplication.processEvents()
            self.ui.label_hatayazi.setText("") #Hatayazinin içindeki text'ti siler.
            QApplication.processEvents()
            self.ui.link_yeri.clear() #Link yerinin içindeki yazıyı temizler.
            QApplication.processEvents()

        except Exception as e:
            print(e)

    def kapat(self):
        os._exit(0) #os ile uygulamayı kapatma.
    def butona_bas(self):
        print("Hello\n")
        self.ui.label_linkbekleniyor2.setText(QCoreApplication.translate("MainWindow","<html><head/><body><p align=\"center\"><span style=\" font-size:7pt; font-weight:600; color:#dfd2d3;\">VİDEO İNDİRİLİYOR</span></p></body></html>"))
        QApplication.processEvents()
        text = self.ui.link_yeri.text()           #Kullanıcının girdiği link"""
        print("Lİmk")
        print(text)
        self.video_indirici(text)                #Burada linki video indirme fonksiyonuna göndereceğiz.

    def indirilenleri_Ac(self):
        path= "C:\\Users\\Admin\\OneDrive\\Masaüstü\\Python_GUİ\\indirilen_videolar"
        os.startfile(path)

    def hata(self):
        print("a")
        try:
            self.ui.labelhataresim = QtWidgets.QLabel(self.ui.groupBox)
            self.ui.labelhataresim.setGeometry(QtCore.QRect(20, 10, 31, 31))
            self.ui.labelhataresim.setStyleSheet("border-image: url(:/ikon/hata.png); background-color: rgb(255,255,0)")
            self.ui.label_hatayazi.setText(QCoreApplication.translate("MainWindow","<html><head/><body><p><span style=\" font-weight:600;\">Hata! Yeniden Deneyin </span></p></body></html>"))
            self.ui.label_linkbekleniyor1.setText(QCoreApplication.translate("MainWindow","<html><head/><body><p align=\"center\"><span style=\" font-size:7pt; font-weight:600; color:#dfd2d3;\">Hata!</span></p></body></html>"))
            self.ui.label_linkbekleniyor2.setText(QCoreApplication.translate("MainWindow","<html><head/><body><p align=\"center\"><span style=\" font-size:7pt; font-weight:600; color:#dfd2d3;\">Hata!</span></p></body></html>"))

            QApplication.processEvents()

            #self.ui.hata()
        except Exception as e:
            print(e)

    def video_indirici(self,link):
         self.ui.label_linkbekleniyor1.setText(QCoreApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt; font-weight:600; color:#dfd2d3;\">LİNK ALINDI</span></p></body></html>"))
         #self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt; font-weight:600; color:#dfd2d3;\">LİNK BEKLENİYOR..</span></p></body></html>"))
         QApplication.processEvents() #İçindeki yazıyı düzletince bu komutu çalıştırıp güncelle.
         try:

             path = "C:\\Users\\Admin\\OneDrive\\Masaüstü\\Python_GUİ\\indirilen_videolar"
             os.chdir(path)
             ydl_opts = {}
             with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
             print("İndirme Tamamlandı!")
             self.ui.label_linkbekleniyor1.setText(QCoreApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt; font-weight:600; color:#dfd2d3;\">YENİ LİNK BEKLENİYOR</span></p></body></html>"))

             self.ui.label_linkbekleniyor2.setText(QCoreApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt; font-weight:600; color:#dfd2d3;\">VİDEO İNDİRİLDİ</span></p></body></html>"))
         except Exception as e:
            #self.ui.push_indir.setText(QCoreApplication.translate("MainWindow", "Hata!!"))
            self.hata()

while True:
    uygulama = QApplication([])
    pencere = dersler_7()
    pencere.show()
    uygulama.exec_()



