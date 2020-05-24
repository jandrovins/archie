from PyQt5 import QtCore, QtGui, QtWidgets

from persistence.FileManager import FileManager
from logic.WebPage import WebPage
from logic.Archiver import Archiver
from main import Ui_Archie


class ArchieView(Ui_Archie):
    def setupUi(self, Archie):
        super(ArchieView, self).setupUi(Archie)

        self.saved_pages_table.setHorizontalHeaderLabels(
            ["Nombre", "Ruta", "Tamaño (MiB)", "Creación", "Tipo"]
        )
        self.push_button_url.clicked.connect(self.archive_by_url)
        self.push_button_topic.clicked.connect(self.archive_by_topic)
        self.push_button_compress.clicked.connect(self.compress)
        self.archiver = Archiver()
        self.webpages = []
        self.populate_webpages_list()
        self.populate_table()

    def populate_webpages_list(self):
        webpages_tuples = FileManager.parse_csv()
        for t in webpages_tuples:
            self.webpages.append(WebPage(t[0], t[1], t[2], t[3], t[4]))

    def populate_table(self):
        row_number = 0
        actual_row_number = self.saved_pages_table.rowCount()
        for webpage in self.webpages:
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
        new_webpage = self.archiver.search_by_url(
            url, download_type, name, FileManager.directory
        )
        self.webpages.append(new_webpage)
        FileManager.persist_webpage(
            new_webpage.name,
            new_webpage.path,
            new_webpage.size,
            new_webpage.creation_date,
            new_webpage.type,
        )
        self.populate_table()

    def archive_by_topic(self):
        # Tomar URL ingresada por el usuario
        topic = self.line_edit_topic.text()
        name = self.line_edit_topic_result_name.text()
        download_type = self.combo_box_topic.currentText()
        new_webpage = self.archiver.search_by_topic(
            topic, download_type, name, FileManager.directory
        )
        self.webpages.append(new_webpage)
        FileManager.persist_webpage(
            new_webpage.name,
            new_webpage.path,
            new_webpage.size,
            new_webpage.creation_date,
            new_webpage.type,
        )
        self.populate_table()

    def compress(self):
        name = self.line_edit_compress.text()
        webpage = None
        for wp in self.webpages:
            if wp.name == name:
                webpage = wp
                break

        if webpage == None:
            return

        webpage.compress()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Archie = QtWidgets.QMainWindow()
    ui = ArchieView()
    ui.setupUi(Archie)
    Archie.show()
    sys.exit(app.exec_())
