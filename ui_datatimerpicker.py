# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_datatimerpicker.ui'
#
# Created: Mon May 21 16:53:49 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_datatimerpicker(object):
    def setupUi(self, datatimerpicker):
        datatimerpicker.setObjectName(_fromUtf8("datatimerpicker"))
        datatimerpicker.resize(692, 394)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(datatimerpicker.sizePolicy().hasHeightForWidth())
        datatimerpicker.setSizePolicy(sizePolicy)
        datatimerpicker.setStyleSheet(_fromUtf8("font: 75 12pt \"Tahoma\";"))
        self.gridLayout = QtGui.QGridLayout(datatimerpicker)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.setasnowbutton = QtGui.QPushButton(datatimerpicker)
        self.setasnowbutton.setObjectName(_fromUtf8("setasnowbutton"))
        self.gridLayout.addWidget(self.setasnowbutton, 0, 0, 1, 4)
        self.label_3 = QtGui.QLabel(datatimerpicker)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label = QtGui.QLabel(datatimerpicker)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(datatimerpicker)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.datepicker = QtGui.QCalendarWidget(datatimerpicker)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.datepicker.sizePolicy().hasHeightForWidth())
        self.datepicker.setSizePolicy(sizePolicy)
        self.datepicker.setObjectName(_fromUtf8("datepicker"))
        self.gridLayout.addWidget(self.datepicker, 2, 0, 1, 1)
        self.hourpicker = QtGui.QListWidget(datatimerpicker)
        self.hourpicker.setStyleSheet(_fromUtf8("font: 75 12pt \"Tahoma\";"))
        self.hourpicker.setObjectName(_fromUtf8("hourpicker"))
        QtGui.QListWidgetItem(self.hourpicker)
        QtGui.QListWidgetItem(self.hourpicker)
        QtGui.QListWidgetItem(self.hourpicker)
        QtGui.QListWidgetItem(self.hourpicker)
        QtGui.QListWidgetItem(self.hourpicker)
        QtGui.QListWidgetItem(self.hourpicker)
        QtGui.QListWidgetItem(self.hourpicker)
        QtGui.QListWidgetItem(self.hourpicker)
        QtGui.QListWidgetItem(self.hourpicker)
        QtGui.QListWidgetItem(self.hourpicker)
        QtGui.QListWidgetItem(self.hourpicker)
        QtGui.QListWidgetItem(self.hourpicker)
        self.gridLayout.addWidget(self.hourpicker, 2, 1, 1, 1)
        self.minutepicker = QtGui.QListWidget(datatimerpicker)
        self.minutepicker.setObjectName(_fromUtf8("minutepicker"))
        QtGui.QListWidgetItem(self.minutepicker)
        QtGui.QListWidgetItem(self.minutepicker)
        QtGui.QListWidgetItem(self.minutepicker)
        QtGui.QListWidgetItem(self.minutepicker)
        QtGui.QListWidgetItem(self.minutepicker)
        QtGui.QListWidgetItem(self.minutepicker)
        QtGui.QListWidgetItem(self.minutepicker)
        QtGui.QListWidgetItem(self.minutepicker)
        QtGui.QListWidgetItem(self.minutepicker)
        QtGui.QListWidgetItem(self.minutepicker)
        QtGui.QListWidgetItem(self.minutepicker)
        QtGui.QListWidgetItem(self.minutepicker)
        self.gridLayout.addWidget(self.minutepicker, 2, 2, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ampmbutton = QtGui.QPushButton(datatimerpicker)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ampmbutton.sizePolicy().hasHeightForWidth())
        self.ampmbutton.setSizePolicy(sizePolicy)
        self.ampmbutton.setMinimumSize(QtCore.QSize(0, 50))
        self.ampmbutton.setCheckable(True)
        self.ampmbutton.setObjectName(_fromUtf8("ampmbutton"))
        self.verticalLayout.addWidget(self.ampmbutton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 2, 3, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(datatimerpicker)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 2, 1, 2)
        self.label_3.setBuddy(self.datepicker)
        self.label.setBuddy(self.hourpicker)
        self.label_2.setBuddy(self.minutepicker)

        self.retranslateUi(datatimerpicker)
        QtCore.QMetaObject.connectSlotsByName(datatimerpicker)

    def retranslateUi(self, datatimerpicker):
        datatimerpicker.setWindowTitle(QtGui.QApplication.translate("datatimerpicker", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.setasnowbutton.setText(QtGui.QApplication.translate("datatimerpicker", "Set as current date and time", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("datatimerpicker", "Date", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("datatimerpicker", "Hours", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("datatimerpicker", "Minutes", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.hourpicker.isSortingEnabled()
        self.hourpicker.setSortingEnabled(False)
        self.hourpicker.item(0).setText(QtGui.QApplication.translate("datatimerpicker", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.hourpicker.item(1).setText(QtGui.QApplication.translate("datatimerpicker", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.hourpicker.item(2).setText(QtGui.QApplication.translate("datatimerpicker", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.hourpicker.item(3).setText(QtGui.QApplication.translate("datatimerpicker", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.hourpicker.item(4).setText(QtGui.QApplication.translate("datatimerpicker", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.hourpicker.item(5).setText(QtGui.QApplication.translate("datatimerpicker", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.hourpicker.item(6).setText(QtGui.QApplication.translate("datatimerpicker", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.hourpicker.item(7).setText(QtGui.QApplication.translate("datatimerpicker", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.hourpicker.item(8).setText(QtGui.QApplication.translate("datatimerpicker", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.hourpicker.item(9).setText(QtGui.QApplication.translate("datatimerpicker", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.hourpicker.item(10).setText(QtGui.QApplication.translate("datatimerpicker", "11", None, QtGui.QApplication.UnicodeUTF8))
        self.hourpicker.item(11).setText(QtGui.QApplication.translate("datatimerpicker", "12", None, QtGui.QApplication.UnicodeUTF8))
        self.hourpicker.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.minutepicker.isSortingEnabled()
        self.minutepicker.setSortingEnabled(False)
        self.minutepicker.item(0).setText(QtGui.QApplication.translate("datatimerpicker", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.minutepicker.item(1).setText(QtGui.QApplication.translate("datatimerpicker", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.minutepicker.item(2).setText(QtGui.QApplication.translate("datatimerpicker", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.minutepicker.item(3).setText(QtGui.QApplication.translate("datatimerpicker", "15", None, QtGui.QApplication.UnicodeUTF8))
        self.minutepicker.item(4).setText(QtGui.QApplication.translate("datatimerpicker", "20", None, QtGui.QApplication.UnicodeUTF8))
        self.minutepicker.item(5).setText(QtGui.QApplication.translate("datatimerpicker", "25", None, QtGui.QApplication.UnicodeUTF8))
        self.minutepicker.item(6).setText(QtGui.QApplication.translate("datatimerpicker", "30", None, QtGui.QApplication.UnicodeUTF8))
        self.minutepicker.item(7).setText(QtGui.QApplication.translate("datatimerpicker", "35", None, QtGui.QApplication.UnicodeUTF8))
        self.minutepicker.item(8).setText(QtGui.QApplication.translate("datatimerpicker", "40", None, QtGui.QApplication.UnicodeUTF8))
        self.minutepicker.item(9).setText(QtGui.QApplication.translate("datatimerpicker", "45", None, QtGui.QApplication.UnicodeUTF8))
        self.minutepicker.item(10).setText(QtGui.QApplication.translate("datatimerpicker", "50", None, QtGui.QApplication.UnicodeUTF8))
        self.minutepicker.item(11).setText(QtGui.QApplication.translate("datatimerpicker", "55", None, QtGui.QApplication.UnicodeUTF8))
        self.minutepicker.setSortingEnabled(__sortingEnabled)
        self.ampmbutton.setText(QtGui.QApplication.translate("datatimerpicker", "AM", None, QtGui.QApplication.UnicodeUTF8))
