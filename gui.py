# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Archie(object):
    def setupUi(self, Archie):
        Archie.setObjectName("Archie")
        Archie.resize(620, 591)
        self.centralwidget = QtWidgets.QWidget(Archie)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 70, 511, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutUrl = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayoutUrl.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutUrl.setObjectName("gridLayoutUrl")
        self.push_button_url = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.push_button_url.setObjectName("push_button_url")
        self.gridLayoutUrl.addWidget(self.push_button_url, 1, 2, 1, 1)
        self.combo_box_url = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.combo_box_url.setInputMethodHints(QtCore.Qt.ImhNone)
        self.combo_box_url.setObjectName("combo_box_url")
        self.combo_box_url.addItem("")
        self.combo_box_url.addItem("")
        self.gridLayoutUrl.addWidget(self.combo_box_url, 1, 1, 1, 1)
        self.line_edit_url = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.line_edit_url.setObjectName("line_edit_url")
        self.gridLayoutUrl.addWidget(self.line_edit_url, 1, 0, 1, 1)
        self.label_url = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_url.setObjectName("label_url")
        self.gridLayoutUrl.addWidget(self.label_url, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 210, 511, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayoutTopic = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayoutTopic.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutTopic.setObjectName("gridLayoutTopic")
        self.push_button_topic = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.push_button_topic.setObjectName("push_button_topic")
        self.gridLayoutTopic.addWidget(self.push_button_topic, 2, 2, 1, 1)
        self.line_edit_topic = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.line_edit_topic.setObjectName("line_edit_topic")
        self.gridLayoutTopic.addWidget(self.line_edit_topic, 2, 0, 1, 1)
        self.combo_box_topic = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.combo_box_topic.setObjectName("combo_box_topic")
        self.combo_box_topic.addItem("")
        self.combo_box_topic.addItem("")
        self.gridLayoutTopic.addWidget(self.combo_box_topic, 2, 1, 1, 1)
        self.label_topic = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_topic.setObjectName("label_topic")
        self.gridLayoutTopic.addWidget(self.label_topic, 0, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(39, 349, 511, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.saved_pages_table = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.saved_pages_table.setColumnCount(5)
        self.saved_pages_table.setObjectName("saved_pages_table")
        self.saved_pages_table.setRowCount(0)
        self.saved_pages_table.horizontalHeader().setCascadingSectionResizes(False)
        self.saved_pages_table.setHorizontalHeaderLabels(
                ['Nombre',
                'Ruta',
                'Tamaño (MiB)',
                'Creación',
                'Tipo']
                )
        self.verticalLayout_4.addWidget(self.saved_pages_table)
        Archie.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Archie)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 20))
        self.menubar.setObjectName("menubar")
        Archie.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Archie)
        self.statusbar.setObjectName("statusbar")
        Archie.setStatusBar(self.statusbar)

        self.retranslateUi(Archie)
        QtCore.QMetaObject.connectSlotsByName(Archie)
        Archie.setTabOrder(self.line_edit_url, self.combo_box_url)
        Archie.setTabOrder(self.combo_box_url, self.push_button_url)
        Archie.setTabOrder(self.push_button_url, self.line_edit_topic)
        Archie.setTabOrder(self.line_edit_topic, self.combo_box_topic)
        Archie.setTabOrder(self.combo_box_topic, self.push_button_topic)

        self.push_button_url.clicked.connect(self.actualizar)    


    def actualizar(self):
        url = self.line_edit_url.text()
        self.label_url.setText(url)
        row_number = self.saved_pages_table.rowCount();
        self.saved_pages_table.insertRow(row_number)
        self.saved_pages_table.setItem(row_number, 0, QtWidgets.QTableWidgetItem(url[0]))
        self.saved_pages_table.setItem(row_number, 1, QtWidgets.QTableWidgetItem(url[1]))
        self.saved_pages_table.setItem(row_number, 2, QtWidgets.QTableWidgetItem(url[2]))
        self.saved_pages_table.setItem(row_number, 3, QtWidgets.QTableWidgetItem(url[3]))
        self.saved_pages_table.setItem(row_number, 4, QtWidgets.QTableWidgetItem(url[4]))



        

    def retranslateUi(self, Archie):
        _translate = QtCore.QCoreApplication.translate
        Archie.setWindowTitle(_translate("Archie", "MainWindow"))
        self.push_button_url.setText(_translate("Archie", "Buscar"))
        self.combo_box_url.setCurrentText(_translate("Archie", "HTML"))
        self.combo_box_url.setItemText(0, _translate("Archie", "HTML"))
        self.combo_box_url.setItemText(1, _translate("Archie", "PDF"))
        self.label_url.setText(_translate("Archie", "Búsqueda por URL"))
        self.push_button_topic.setText(_translate("Archie", "Buscar"))
        self.combo_box_topic.setCurrentText(_translate("Archie", "HTML"))
        self.combo_box_topic.setItemText(0, _translate("Archie", "HTML"))
        self.combo_box_topic.setItemText(1, _translate("Archie", "PDF"))
        self.label_topic.setText(_translate("Archie", "Búsqueda por tema"))
        self.label.setText(_translate("Archie", "Páginas guardadas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Archie = QtWidgets.QMainWindow()
    ui = Ui_Archie()
    ui.setupUi(Archie)
    Archie.show()
    sys.exit(app.exec_())

