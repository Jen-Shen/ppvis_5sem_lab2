# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/design/action.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_choose(object):
    def setupUi(self, choose):
        choose.setObjectName("choose")
        choose.resize(190, 206)
        choose.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(choose)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("background-color: rgb(106, 90, 205);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("background-color: rgb(106, 90, 205);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setStyleSheet("background-color: rgb(106, 90, 205);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setStyleSheet("background-color: rgb(106, 90, 205);")
        self.pushButton_4.setObjectName("pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setStyleSheet("background-color: rgb(106, 90, 205);")
        self.pushButton_5.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        choose.setCentralWidget(self.centralwidget)

        self.retranslateUi(choose)
        QtCore.QMetaObject.connectSlotsByName(choose)

    def retranslateUi(self, choose):
        _translate = QtCore.QCoreApplication.translate
        choose.setWindowTitle(_translate("choose", "MainWindow"))
        self.label.setText(_translate("choose", "               Действия"))
        self.pushButton.setText(_translate("choose", "Просмотр"))
        self.pushButton_2.setText(_translate("choose", "Добавить рецепт"))
        self.pushButton_3.setText(_translate("choose", "Изменить рецепт"))
        self.pushButton_4.setText(_translate("choose", "Удалить рецепт"))
        self.pushButton_5.setText(_translate("choose", "Вернуться назад"))
