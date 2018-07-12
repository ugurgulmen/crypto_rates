# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from datetime import datetime


class Ui_Form(object):
    url = 'https://www.btcturk.com/api/ticker'
    response = requests.get(url)
    json_data = response.json()
    currency1_list = []
    currency2_list = []
    pair_list = []

    for i in json_data:
        if i["pair"] not in pair_list:
            pair_list.append(i["pair"])
        if i["numeratorsymbol"] not in currency1_list:
            currency1_list.append(i["numeratorsymbol"])
        if i["denominatorsymbol"] not in currency2_list:
            currency2_list.append(i["denominatorsymbol"])
    
    currency1_list.sort()
    currency2_list.sort()
            
    def calc(self):
        currency1 = str(self.currency1.currentText())
        currency2 = str(self.currency2.currentText())
        pair = currency1 + currency2

        if pair in self.pair_list:
            try:
                response = requests.get(self.url)
                json_data = response.json()
                for i in json_data:
                    if pair in i['pair']:
                        amount = float(self.amount.text())
                        total = i["last"] * amount
                        self.total.setText(str('{:.2f}'.format(total)) + ' ' + str(self.currency2.currentText()))
                        self.date.setText(str(datetime.fromtimestamp(i["timestamp"])))
            except ValueError:
                self.total.setText('Please enter a value.')
        else:
            self.total.setText('N/A')
            self.date.setText('N/A')

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(544, 183)
        Form.setFixedSize(Form.size())
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 531, 171))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.amount = QtWidgets.QLineEdit(self.widget)
        self.amount.setObjectName("amount")
        self.horizontalLayout.addWidget(self.amount)
        self.currency1 = QtWidgets.QComboBox(self.widget)
        self.currency1.setObjectName("currency1")
        self.currency1.addItems(self.currency1_list)
        self.horizontalLayout.addWidget(self.currency1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.currency2 = QtWidgets.QComboBox(self.widget)
        self.currency2.setObjectName("currency2")
        self.currency2.addItems(self.currency2_list)
        self.horizontalLayout.addWidget(self.currency2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.total = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.total.setFont(font)
        self.total.setText("")
        self.total.setAlignment(QtCore.Qt.AlignCenter)
        self.total.setObjectName("total")
        self.verticalLayout.addWidget(self.total)
        self.date = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.date.setFont(font)
        self.date.setText("")
        self.date.setAlignment(QtCore.Qt.AlignCenter)
        self.date.setObjectName("date")
        self.verticalLayout.addWidget(self.date)

        self.pushButton.clicked.connect(self.calc)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cryptocurrency Exhcange Rates"))
        self.label.setText(_translate("Form", "to"))
        self.pushButton.setText(_translate("Form", "Calculate"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

