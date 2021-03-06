# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'C:\Users\David Mitchell\Desktop\Programming\Python\qtPy\MadiRadio UI designer\MadiRadioUI2NameWindow.ui'
# Created by: PyQt5 UI code generator 5.15.4
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
# from MadiRadioUI1MainWindow import MainWindow as Main

class Ui_MainWindowName(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindowName")
        MainWindow.resize(1000, 900)
        MainWindow.setMinimumSize(QtCore.QSize(550, 500))
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(50, 50, 50, 50)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMaxVisibleItems(6)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox.setIconSize(QtCore.QSize(16, 12))
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)
        self.donePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.donePushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.donePushButton.setObjectName("donePushButton")
        self.donePushButton.clicked.connect(lambda: self.selectNamenColour())
        self.gridLayout.addWidget(self.donePushButton, 4, 0, 1, 2)
        self.nameEntryField = QtWidgets.QLineEdit(self.centralwidget)
        self.nameEntryField.setObjectName("nameEntryField")
        self.gridLayout.addWidget(self.nameEntryField, 0, 1, 1, 1)
        self.colour_label = QtWidgets.QLabel(self.centralwidget)
        self.colour_label.setObjectName("colour_label")
        self.gridLayout.addWidget(self.colour_label, 1, 0, 1, 1)
        self.gridLayout.setRowMinimumHeight(0, 1)
        self.gridLayout.setRowMinimumHeight(4, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(4, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindowName):
        _translate = QtCore.QCoreApplication.translate
        MainWindowName.setWindowTitle(_translate("MainWindowName", "Madi Radio - Name"))
        MainWindowName.setStyleSheet('''
        .QMainWindow{
            background-color: rgba(38,8,24,255);
        }
        .QLabel{
            color:white;
        }
        .QLineEdit{
            color: white;
            border: 3px solid #440f2b;
            background-color: #4c1130;
            padding: 5px,5px;
            padding-left: 10px;
            margin-right: 50%;
            margin-left: 10%;
            border-radius: 15px;
        }
        .QLineEdit:hover{
            border: 3px solid #6b1e47;
            background-color: #591539;
        }
        .QLineEdit:focus{
            background-color: #591539;
            border-color: #6b1e47;
        }
        .QComboBox{
            color: white;
            border: 3px solid #440f2b;
            background-color: #4c1130;
            padding: 5px,5px;
            padding-left: 10px;
            margin-right: 50%;
            margin-left: 10%;
            border-radius: 15px;
        }
        .QComboBox:hover{
            border: 3px solid #6b1e47;
            background-color: #591539;
        }
        .QComboBox:focus{
            background-color: #591539;
            border-color: #6b1e47;
        }
        .QPushButton{
            border: 3px solid #440f2b;
            border-style: outset;
            background-color: #4c1130;
            color: white;
            margin-left: 100px;
            margin-right: 100px;
            padding: 5px;
            border-radius: 15px;
        }
        .QPushButton::hover{
            border: 3px solid #6b1e47;
            background-color: #591539;
            color: pink;
        }
        ''')
        self.comboBox.setItemText(0, _translate("MainWindowName", "Blue"))
        self.comboBox.setItemText(1, _translate("MainWindowName", "Red"))
        self.comboBox.setItemText(2, _translate("MainWindowName", "Yellow"))
        self.comboBox.setItemText(3, _translate("MainWindowName", "Green"))
        self.comboBox.setItemText(4, _translate("MainWindowName", "Purple"))
        self.comboBox.setItemText(5, _translate("MainWindowName", "Pink"))
        self.comboBox.setStyleSheet('''
            QListView{
            }
            QListView::item {
                color: white;
                background-color: #4c1130;
                padding: 5px;
            }
            QListView::item::hover {
                background-color: #6f4059;
                border-left: 3px solid white;
            }
        ''')
        self.name_label.setText(_translate("MainWindowName", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Name :      </span></p></body></html>"))
        self.donePushButton.setText(_translate("MainWindowName", "Done"))
        self.colour_label.setText(_translate("MainWindowName", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Colour : </span></p></body></html>"))

    def select_NameColour(self):
        msgPOP = QtWidgets.QMessageBox()
        name = self.nameEntryField.text()
        color = self.comboBox.currentText()
        if name and color:
            msgPOP.setWindowTitle("Done!")
            msgPOP.setText(f"Name: {name} and Color: {color} has been set.")
            msgPOP.setIcon(QtWidgets.QMessageBox.Icon.Information)
        else:
            msgPOP.setWindowTitle("Issue!")
            msgPOP.setText("Please make sure to choose a name and a color :)")
            msgPOP.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msgPOP.exec_()

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindowName()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
