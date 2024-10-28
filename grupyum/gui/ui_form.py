# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QProgressBar, QPushButton, QSizePolicy, QWidget)

class Ui_Grupy1(object):
    def setupUi(self, Grupy1):
        if not Grupy1.objectName():
            Grupy1.setObjectName(u"Grupy1")
        Grupy1.resize(691, 482)
        self.label = QLabel(Grupy1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 191, 16))
        self.importButton = QPushButton(Grupy1)
        self.importButton.setObjectName(u"importButton")
        self.importButton.setGeometry(QRect(200, 10, 80, 23))
        self.list_selected_images = QListWidget(Grupy1)
        self.list_selected_images.setObjectName(u"list_selected_images")
        self.list_selected_images.setGeometry(QRect(20, 40, 256, 291))
        self.loadButton = QPushButton(Grupy1)
        self.loadButton.setObjectName(u"loadButton")
        self.loadButton.setGeometry(QRect(90, 340, 101, 23))
        self.load_OK = QLabel(Grupy1)
        self.load_OK.setObjectName(u"load_OK")
        self.load_OK.setGeometry(QRect(110, 360, 71, 20))
        self.codes_list = QListWidget(Grupy1)
        self.codes_list.setObjectName(u"codes_list")
        self.codes_list.setGeometry(QRect(420, 40, 256, 291))
        self.exportButton = QPushButton(Grupy1)
        self.exportButton.setObjectName(u"exportButton")
        self.exportButton.setGeometry(QRect(490, 340, 101, 23))
        self.load_OK_2 = QLabel(Grupy1)
        self.load_OK_2.setObjectName(u"load_OK_2")
        self.load_OK_2.setGeometry(QRect(510, 360, 61, 20))
        self.processButton = QPushButton(Grupy1)
        self.processButton.setObjectName(u"processButton")
        self.processButton.setGeometry(QRect(300, 180, 101, 23))
        self.progressBar = QProgressBar(Grupy1)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(290, 210, 118, 23))
        self.progressBar.setValue(0)

        self.retranslateUi(Grupy1)

        QMetaObject.connectSlotsByName(Grupy1)
    # setupUi

    def retranslateUi(self, Grupy1):
        Grupy1.setWindowTitle(QCoreApplication.translate("Grupy1", u"Grupy1", None))
        self.label.setText(QCoreApplication.translate("Grupy1", u"Carregue uma ou mais imagens", None))
        self.importButton.setText(QCoreApplication.translate("Grupy1", u"Carregar", None))
        self.loadButton.setText(QCoreApplication.translate("Grupy1", u"Carregar", None))
        self.load_OK.setText(QCoreApplication.translate("Grupy1", u"Carregado", None))
        self.exportButton.setText(QCoreApplication.translate("Grupy1", u"Exportar", None))
        self.load_OK_2.setText(QCoreApplication.translate("Grupy1", u"Exportado", None))
        self.processButton.setText(QCoreApplication.translate("Grupy1", u"Processar", None))
    # retranslateUi

