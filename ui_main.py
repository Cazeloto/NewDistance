# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cdist.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(674, 400)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 10, 181, 41))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 60, 661, 181))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 321, 81))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_cidades = QLabel(self.frame_3)
        self.lbl_cidades.setObjectName(u"lbl_cidades")

        self.verticalLayout.addWidget(self.lbl_cidades)

        self.txt_cidades = QLineEdit(self.frame_3)
        self.txt_cidades.setObjectName(u"txt_cidades")
        self.txt_cidades.setStyleSheet(u"background-color: rgb(251, 255, 206);")

        self.verticalLayout.addWidget(self.txt_cidades)

        self.btn_cidades = QPushButton(self.frame_3)
        self.btn_cidades.setObjectName(u"btn_cidades")

        self.verticalLayout.addWidget(self.btn_cidades, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(330, 0, 331, 81))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_bases = QLabel(self.frame_4)
        self.lbl_bases.setObjectName(u"lbl_bases")

        self.verticalLayout_2.addWidget(self.lbl_bases)

        self.txt_bases = QLineEdit(self.frame_4)
        self.txt_bases.setObjectName(u"txt_bases")
        self.txt_bases.setStyleSheet(u"background-color: rgb(251, 255, 206);")

        self.verticalLayout_2.addWidget(self.txt_bases)

        self.btn_bases = QPushButton(self.frame_4)
        self.btn_bases.setObjectName(u"btn_bases")

        self.verticalLayout_2.addWidget(self.btn_bases, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 90, 321, 81))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_saida = QLabel(self.frame_5)
        self.lbl_saida.setObjectName(u"lbl_saida")

        self.verticalLayout_3.addWidget(self.lbl_saida)

        self.txt_saida = QLineEdit(self.frame_5)
        self.txt_saida.setObjectName(u"txt_saida")
        self.txt_saida.setMinimumSize(QSize(0, 19))
        self.txt_saida.setStyleSheet(u"background-color: rgb(251, 255, 206);")

        self.verticalLayout_3.addWidget(self.txt_saida)

        self.btn_saida = QPushButton(self.frame_5)
        self.btn_saida.setObjectName(u"btn_saida")

        self.verticalLayout_3.addWidget(self.btn_saida, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(330, 90, 331, 81))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_bing = QLabel(self.frame_6)
        self.lbl_bing.setObjectName(u"lbl_bing")

        self.verticalLayout_5.addWidget(self.lbl_bing)

        self.txt_bing = QLineEdit(self.frame_6)
        self.txt_bing.setObjectName(u"txt_bing")
        self.txt_bing.setStyleSheet(u"background-color: rgb(251, 255, 206);")

        self.verticalLayout_5.addWidget(self.txt_bing)

        self.btn_bing = QPushButton(self.frame_6)
        self.btn_bing.setObjectName(u"btn_bing")

        self.verticalLayout_5.addWidget(self.btn_bing, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 180, 461, 31))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(190, 10, 91, 20))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 280, 621, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(0, 290, 661, 101))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(0, 10, 631, 41))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_cidade_status = QLabel(self.frame_8)
        self.lbl_cidade_status.setObjectName(u"lbl_cidade_status")

        self.gridLayout.addWidget(self.lbl_cidade_status, 0, 0, 1, 1)

        self.lbl_console = QLabel(self.frame_7)
        self.lbl_console.setObjectName(u"lbl_console")
        self.lbl_console.setGeometry(QRect(10, 50, 431, 31))
        self.btn_processa = QPushButton(self.centralwidget)
        self.btn_processa.setObjectName(u"btn_processa")
        self.btn_processa.setGeometry(QRect(290, 250, 81, 31))
        self.btn_processa.setStyleSheet(u"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">C\u00e1lculo de Dist\u00e2ncias</span></p></body></html>", None))
        self.lbl_cidades.setText(QCoreApplication.translate("MainWindow", u"Cidades", None))
        self.btn_cidades.setText(QCoreApplication.translate("MainWindow", u"Procurar", None))
        self.lbl_bases.setText(QCoreApplication.translate("MainWindow", u"Bases", None))
        self.btn_bases.setText(QCoreApplication.translate("MainWindow", u"Procurar", None))
        self.lbl_saida.setText(QCoreApplication.translate("MainWindow", u"Pasta Saida", None))
        self.btn_saida.setText(QCoreApplication.translate("MainWindow", u"Procurar", None))
        self.lbl_bing.setText(QCoreApplication.translate("MainWindow", u"Chave Bing", None))
        self.btn_bing.setText(QCoreApplication.translate("MainWindow", u"Procurar", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.lbl_cidade_status.setText(QCoreApplication.translate("MainWindow", u"Cidades", None))
        self.lbl_console.setText("")
        self.btn_processa.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
    # retranslateUi

