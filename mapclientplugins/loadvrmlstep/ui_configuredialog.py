# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/configuredialog.ui'
#
# Created: Wed Mar 18 12:14:12 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(418, 303)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.configGroupBox = QtGui.QGroupBox(Dialog)
        self.configGroupBox.setTitle("")
        self.configGroupBox.setObjectName("configGroupBox")
        self.formLayout = QtGui.QFormLayout(self.configGroupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.idLabel = QtGui.QLabel(self.configGroupBox)
        self.idLabel.setObjectName("idLabel")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.idLabel)
        self.idLineEdit = QtGui.QLineEdit(self.configGroupBox)
        self.idLineEdit.setObjectName("idLineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.idLineEdit)
        self.filenameLabel = QtGui.QLabel(self.configGroupBox)
        self.filenameLabel.setObjectName("filenameLabel")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.filenameLabel)
        self.modelIndexLabel = QtGui.QLabel(self.configGroupBox)
        self.modelIndexLabel.setObjectName("modelIndexLabel")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.modelIndexLabel)
        self.modelIndexLineEdit = QtGui.QLineEdit(self.configGroupBox)
        self.modelIndexLineEdit.setObjectName("modelIndexLineEdit")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.modelIndexLineEdit)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.filenameLineEdit = QtGui.QLineEdit(self.configGroupBox)
        self.filenameLineEdit.setObjectName("filenameLineEdit")
        self.horizontalLayout_2.addWidget(self.filenameLineEdit)
        self.filenamePushButton = QtGui.QPushButton(self.configGroupBox)
        self.filenamePushButton.setDefault(False)
        self.filenamePushButton.setFlat(False)
        self.filenamePushButton.setObjectName("filenamePushButton")
        self.horizontalLayout_2.addWidget(self.filenamePushButton)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.idLineEdit, self.filenameLineEdit)
        Dialog.setTabOrder(self.filenameLineEdit, self.filenamePushButton)
        Dialog.setTabOrder(self.filenamePushButton, self.modelIndexLineEdit)
        Dialog.setTabOrder(self.modelIndexLineEdit, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Configure Load VRML Step", None, QtGui.QApplication.UnicodeUTF8))
        self.idLabel.setText(QtGui.QApplication.translate("Dialog", "Identifier:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.filenameLabel.setText(QtGui.QApplication.translate("Dialog", "Filename:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.modelIndexLabel.setText(QtGui.QApplication.translate("Dialog", "Model Number:", None, QtGui.QApplication.UnicodeUTF8))
        self.filenamePushButton.setText(QtGui.QApplication.translate("Dialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))

