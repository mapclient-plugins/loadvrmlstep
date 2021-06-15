# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(418, 303)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.configGroupBox = QGroupBox(Dialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.idLabel = QLabel(self.configGroupBox)
        self.idLabel.setObjectName(u"idLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.idLabel)

        self.idLineEdit = QLineEdit(self.configGroupBox)
        self.idLineEdit.setObjectName(u"idLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.idLineEdit)

        self.filenameLabel = QLabel(self.configGroupBox)
        self.filenameLabel.setObjectName(u"filenameLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.filenameLabel)

        self.modelIndexLabel = QLabel(self.configGroupBox)
        self.modelIndexLabel.setObjectName(u"modelIndexLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.modelIndexLabel)

        self.modelIndexLineEdit = QLineEdit(self.configGroupBox)
        self.modelIndexLineEdit.setObjectName(u"modelIndexLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.modelIndexLineEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.filenameLineEdit = QLineEdit(self.configGroupBox)
        self.filenameLineEdit.setObjectName(u"filenameLineEdit")

        self.horizontalLayout_2.addWidget(self.filenameLineEdit)

        self.filenamePushButton = QPushButton(self.configGroupBox)
        self.filenamePushButton.setObjectName(u"filenamePushButton")
        self.filenamePushButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.filenamePushButton)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_2)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        QWidget.setTabOrder(self.idLineEdit, self.filenameLineEdit)
        QWidget.setTabOrder(self.filenameLineEdit, self.filenamePushButton)
        QWidget.setTabOrder(self.filenamePushButton, self.modelIndexLineEdit)
        QWidget.setTabOrder(self.modelIndexLineEdit, self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.filenamePushButton.setDefault(False)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Configure Load VRML Step", None))
        self.configGroupBox.setTitle("")
        self.idLabel.setText(QCoreApplication.translate("Dialog", u"Identifier:  ", None))
        self.filenameLabel.setText(QCoreApplication.translate("Dialog", u"Filename:  ", None))
        self.modelIndexLabel.setText(QCoreApplication.translate("Dialog", u"Model Number:", None))
        self.filenamePushButton.setText(QCoreApplication.translate("Dialog", u"Browse", None))
    # retranslateUi

