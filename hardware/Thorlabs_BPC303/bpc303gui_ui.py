# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bpc303gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(560, 603)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 502, 561))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.isDeviceConnected = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.isDeviceConnected.sizePolicy().hasHeightForWidth())
        self.isDeviceConnected.setSizePolicy(sizePolicy)
        self.isDeviceConnected.setMinimumSize(QtCore.QSize(30, 30))
        self.isDeviceConnected.setMaximumSize(QtCore.QSize(30, 30))
        self.isDeviceConnected.setBaseSize(QtCore.QSize(30, 30))
        self.isDeviceConnected.setAutoFillBackground(False)
        self.isDeviceConnected.setStyleSheet(_fromUtf8("background-color: lightgrey;"))
        self.isDeviceConnected.setFrameShape(QtWidgets.QFrame.Panel)
        self.isDeviceConnected.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.isDeviceConnected.setLineWidth(1)
        self.isDeviceConnected.setText(_fromUtf8(""))
        self.isDeviceConnected.setAlignment(QtCore.Qt.AlignCenter)
        self.isDeviceConnected.setObjectName(_fromUtf8("isDeviceConnected"))
        self.gridLayout.addWidget(self.isDeviceConnected, 2, 7, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 8, 1, 1)
        self.deviceInfo = QtWidgets.QPlainTextEdit(self.groupBox)
        self.deviceInfo.setReadOnly(True)
        self.deviceInfo.setPlainText(_fromUtf8("No device connected"))
        self.deviceInfo.setObjectName(_fromUtf8("deviceInfo"))
        self.gridLayout.addWidget(self.deviceInfo, 4, 1, 1, 8)
        self.connectDevice = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectDevice.sizePolicy().hasHeightForWidth())
        self.connectDevice.setSizePolicy(sizePolicy)
        self.connectDevice.setObjectName(_fromUtf8("connectDevice"))
        self.gridLayout.addWidget(self.connectDevice, 2, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 6, 1, 1)
        self.deviceID = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deviceID.sizePolicy().hasHeightForWidth())
        self.deviceID.setSizePolicy(sizePolicy)
        self.deviceID.setFrame(True)
        self.deviceID.setObjectName(_fromUtf8("deviceID"))
        self.gridLayout.addWidget(self.deviceID, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.setZero = QtWidgets.QPushButton(self.groupBox_3)
        self.setZero.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setZero.sizePolicy().hasHeightForWidth())
        self.setZero.setSizePolicy(sizePolicy)
        self.setZero.setObjectName(_fromUtf8("setZero"))
        self.gridLayout_2.addWidget(self.setZero, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 0, 1, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 1, 2, 1, 1)
        self.setPosition = QtWidgets.QPushButton(self.groupBox_3)
        self.setPosition.setEnabled(False)
        self.setPosition.setObjectName(_fromUtf8("setPosition"))
        self.gridLayout_2.addWidget(self.setPosition, 2, 0, 1, 1)
        self.xPos = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xPos.sizePolicy().hasHeightForWidth())
        self.xPos.setSizePolicy(sizePolicy)
        self.xPos.setObjectName(_fromUtf8("xPos"))
        self.gridLayout_2.addWidget(self.xPos, 2, 1, 1, 1)
        self.yPos = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yPos.sizePolicy().hasHeightForWidth())
        self.yPos.setSizePolicy(sizePolicy)
        self.yPos.setObjectName(_fromUtf8("yPos"))
        self.gridLayout_2.addWidget(self.yPos, 2, 2, 1, 1)
        self.zPos = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zPos.sizePolicy().hasHeightForWidth())
        self.zPos.setSizePolicy(sizePolicy)
        self.zPos.setObjectName(_fromUtf8("zPos"))
        self.gridLayout_2.addWidget(self.zPos, 2, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.groupBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.axisToIdentify = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisToIdentify.sizePolicy().hasHeightForWidth())
        self.axisToIdentify.setSizePolicy(sizePolicy)
        self.axisToIdentify.setFrame(True)
        self.axisToIdentify.setObjectName(_fromUtf8("axisToIdentify"))
        self.axisToIdentify.addItem(_fromUtf8(""))
        self.axisToIdentify.setItemText(0, _fromUtf8("x"))
        self.axisToIdentify.addItem(_fromUtf8(""))
        self.axisToIdentify.setItemText(1, _fromUtf8("y"))
        self.axisToIdentify.addItem(_fromUtf8(""))
        self.axisToIdentify.setItemText(2, _fromUtf8("z"))
        self.horizontalLayout.addWidget(self.axisToIdentify)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.identifyDevice = QtWidgets.QPushButton(self.groupBox_2)
        self.identifyDevice.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.identifyDevice.sizePolicy().hasHeightForWidth())
        self.identifyDevice.setSizePolicy(sizePolicy)
        self.identifyDevice.setAutoDefault(False)
        self.identifyDevice.setDefault(False)
        self.identifyDevice.setFlat(False)
        self.identifyDevice.setObjectName(_fromUtf8("identifyDevice"))
        self.horizontalLayout.addWidget(self.identifyDevice)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "Connection", None))
        self.label_2.setText(_translate("MainWindow", " Instrument ID", None))
        self.connectDevice.setText(_translate("MainWindow", "Connect", None))
        self.deviceID.setToolTip(_translate("MainWindow", "<html><head/><body><p>tooltest</p></body></html>", None))
        self.deviceID.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>test</p></body></html>", None))
        self.deviceID.setText(_translate("MainWindow", "71254674", None))
        self.deviceID.setPlaceholderText(_translate("MainWindow", "71254674", None))
        self.label.setText(_translate("MainWindow", "Device Info", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Stage control", None))
        self.setZero.setText(_translate("MainWindow", "Zero piezos", None))
        self.label_4.setText(_translate("MainWindow", "z", None))
        self.label_3.setText(_translate("MainWindow", "x", None))
        self.label_5.setText(_translate("MainWindow", "y", None))
        self.setPosition.setText(_translate("MainWindow", "Go to:", None))
        self.xPos.setSuffix(_translate("MainWindow", " um", None))
        self.yPos.setSuffix(_translate("MainWindow", " um", None))
        self.zPos.setSuffix(_translate("MainWindow", " um", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Utilities", None))
        self.identifyDevice.setText(_translate("MainWindow", "Identify axis", None))
