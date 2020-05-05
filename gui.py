# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from WgetWrapper import WgetWrapper
from FileManager import FileManager
from Archiver import Archiver
from WebPage import WebPage


class Ui_Archie(object):
    def setupUi(self, Archie):
        Archie.setObjectName("Archie")
        Archie.resize(601, 563)
        self.centralwidget = QtWidgets.QWidget(Archie)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 20, 511, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutUrl = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayoutUrl.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutUrl.setObjectName("gridLayoutUrl")
        self.label_url = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_url.setObjectName("label_url")
        self.gridLayoutUrl.addWidget(self.label_url, 1, 0, 1, 1)
        self.push_button_url = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.push_button_url.setObjectName("push_button_url")
        self.gridLayoutUrl.addWidget(self.push_button_url, 2, 3, 1, 1)
        self.combo_box_url = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.combo_box_url.setInputMethodHints(QtCore.Qt.ImhNone)
        self.combo_box_url.setObjectName("combo_box_url")
        self.combo_box_url.addItem("")
        self.combo_box_url.addItem("")
        self.gridLayoutUrl.addWidget(self.combo_box_url, 2, 2, 1, 1)
        self.line_edit_url = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.line_edit_url.setObjectName("line_edit_url")
        self.gridLayoutUrl.addWidget(self.line_edit_url, 2, 0, 1, 1)
        self.line_edit_url_result_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.line_edit_url_result_name.setObjectName("line_edit_url_result_name")
        self.gridLayoutUrl.addWidget(self.line_edit_url_result_name, 2, 1, 1, 1)
        self.label_search_url = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_search_url.setObjectName("label_search_url")
        self.gridLayoutUrl.addWidget(self.label_search_url, 0, 1, 1, 1)
        self.label_url_resultado = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_url_resultado.setObjectName("label_url_resultado")
        self.gridLayoutUrl.addWidget(self.label_url_resultado, 1, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 130, 511, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayoutTopic = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayoutTopic.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutTopic.setObjectName("gridLayoutTopic")
        self.push_button_topic = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.push_button_topic.setObjectName("push_button_topic")
        self.gridLayoutTopic.addWidget(self.push_button_topic, 3, 3, 1, 1)
        self.line_edit_topic = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.line_edit_topic.setObjectName("line_edit_topic")
        self.gridLayoutTopic.addWidget(self.line_edit_topic, 3, 0, 1, 1)
        self.combo_box_topic = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.combo_box_topic.setObjectName("combo_box_topic")
        self.combo_box_topic.addItem("")
        self.combo_box_topic.addItem("")
        self.gridLayoutTopic.addWidget(self.combo_box_topic, 3, 2, 1, 1)
        self.label_topic = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_topic.setObjectName("label_topic")
        self.gridLayoutTopic.addWidget(self.label_topic, 1, 0, 1, 1)
        self.line_edit_topic_result_name = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.line_edit_topic_result_name.setObjectName("line_edit_topic_result_name")
        self.gridLayoutTopic.addWidget(self.line_edit_topic_result_name, 3, 1, 1, 1)
        self.label_search_url_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_search_url_2.setObjectName("label_search_url_2")
        self.gridLayoutTopic.addWidget(self.label_search_url_2, 0, 1, 1, 1)
        self.label_url_resultado_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_url_resultado_2.setObjectName("label_url_resultado_2")
        self.gridLayoutTopic.addWidget(self.label_url_resultado_2, 1, 1, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 240, 511, 181))
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
        self.verticalLayout_4.addWidget(self.saved_pages_table)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 450, 511, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_compress = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_compress.setObjectName("label_compress")
        self.horizontalLayout.addWidget(self.label_compress)
        self.line_edit_compress = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.line_edit_compress.setObjectName("line_edit_compress")
        self.horizontalLayout.addWidget(self.line_edit_compress)
        self.push_button_compress = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.push_button_compress.setObjectName("push_button_compress")
        self.horizontalLayout.addWidget(self.push_button_compress)
        Archie.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Archie)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 20))
        self.menubar.setObjectName("menubar")
        Archie.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Archie)
        self.statusbar.setObjectName("statusbar")
        Archie.setStatusBar(self.statusbar)

        self.retranslateUi(Archie)
        QtCore.QMetaObject.connectSlotsByName(Archie)
        Archie.setTabOrder(self.line_edit_url, self.line_edit_url_result_name)
        Archie.setTabOrder(self.line_edit_url_result_name, self.combo_box_url)
        Archie.setTabOrder(self.combo_box_url, self.push_button_url)
        Archie.setTabOrder(self.push_button_url, self.line_edit_topic)
        Archie.setTabOrder(self.line_edit_topic, self.line_edit_topic_result_name)
        Archie.setTabOrder(self.line_edit_topic_result_name, self.combo_box_topic)
        Archie.setTabOrder(self.combo_box_topic, self.push_button_topic)
        Archie.setTabOrder(self.push_button_topic, self.saved_pages_table)
        Archie.setTabOrder(self.saved_pages_table, self.line_edit_compress)
        Archie.setTabOrder(self.line_edit_compress, self.push_button_compress)

        self.saved_pages_table.setHorizontalHeaderLabels(
            ["Nombre", "Ruta", "Tamaño (MiB)", "Creación", "Tipo"]
        )
        self.push_button_url.clicked.connect(self.archive_by_url)
        self.push_button_topic.clicked.connect(self.archive_by_topic)
        self.push_button_compress.clicked.connect(self.compress)
        self.archiver = Archiver()
        FileManager.parse_csv()
        self.populate_table()

    def retranslateUi(self, Archie):
        _translate = QtCore.QCoreApplication.translate
        Archie.setWindowTitle(_translate("Archie", "MainWindow"))
        self.label_url.setText(_translate("Archie", "URL"))
        self.push_button_url.setText(_translate("Archie", "Buscar"))
        self.combo_box_url.setCurrentText(_translate("Archie", "HTML"))
        self.combo_box_url.setItemText(0, _translate("Archie", "HTML"))
        self.combo_box_url.setItemText(1, _translate("Archie", "PDF"))
        self.label_search_url.setText(_translate("Archie", "Búsqueda por URL"))
        self.label_url_resultado.setText(_translate("Archie", "Nombre del resultado"))
        self.push_button_topic.setText(_translate("Archie", "Buscar"))
        self.combo_box_topic.setCurrentText(_translate("Archie", "HTML"))
        self.combo_box_topic.setItemText(0, _translate("Archie", "HTML"))
        self.combo_box_topic.setItemText(1, _translate("Archie", "PDF"))
        self.label_topic.setText(_translate("Archie", "Tema"))
        self.label_search_url_2.setText(_translate("Archie", "Búsqueda por tema"))
        self.label_url_resultado_2.setText(_translate("Archie", "Nombre del resultado"))
        self.label.setText(_translate("Archie", "Páginas guardadas"))
        self.label_compress.setText(_translate("Archie", "Página a comprimir"))
        self.push_button_compress.setText(_translate("Archie", "Compress"))

    def populate_table(self):
        row_number = 0
        actual_row_number = self.saved_pages_table.rowCount()
        for webpage in FileManager.webpages:
            if row_number >= actual_row_number:
                self.saved_pages_table.insertRow(row_number)

            name = webpage.name
            abs_path = str(webpage.path)
            size = str(webpage.size)
            creation_date_str = webpage.creation_date.strftime("%Y-%m-%d")
            page_type = webpage.type

            self.saved_pages_table.setItem(
                row_number, 0, QtWidgets.QTableWidgetItem(name)
            )
            self.saved_pages_table.setItem(
                row_number, 1, QtWidgets.QTableWidgetItem(abs_path)
            )
            self.saved_pages_table.setItem(
                row_number, 2, QtWidgets.QTableWidgetItem(size)
            )
            self.saved_pages_table.setItem(
                row_number, 3, QtWidgets.QTableWidgetItem(creation_date_str)
            )
            self.saved_pages_table.setItem(
                row_number, 4, QtWidgets.QTableWidgetItem(page_type)
            )

            row_number += 1

    def archive_by_url(self):
        # Tomar URL ingresada por el usuario
        url = self.line_edit_url.text()
        name = self.line_edit_url_result_name.text()
        download_type = self.combo_box_url.currentText()
        new_webpage = self.archiver.search_by_url(url, download_type, name)
        print(type(new_webpage))
        FileManager.add_webpage(new_webpage)
        self.populate_table()

    def archive_by_topic(self):
        # Tomar URL ingresada por el usuario
        topic = self.line_edit_topic.text()
        name = self.line_edit_topic_result_name.text()
        download_type = self.combo_box_topic.currentText()
        new_webpage = self.archiver.search_by_topic(topic, download_type, name)
        FileManager.add_webpage(new_webpage)
        self.populate_table()

    def compress(self):
        name = self.line_edit_compress.text()
        webpage = None
        for wp in FileManager.webpages:
            if wp.name == name:
                webpage = wp
                break

        if webpage == None:
            return

        FileManager.compress(webpage)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Archie = QtWidgets.QMainWindow()
    ui = Ui_Archie()
    ui.setupUi(Archie)
    Archie.show()
    sys.exit(app.exec_())
