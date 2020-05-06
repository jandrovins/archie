from pathlib import Path
import shutil


class WebPage:
    def __init__(self, name, creation_date, size, path):
        self.name = name
        self.creation_date = creation_date
        self.size = size
        self.path = path


class WebPagePDF(WebPage):
    prefix = Path.home() / Path("Documents/Archie/PDF/")

    def __init__(self, name, creation_date, size, path):
        super(WebPagePDF, self).__init__(name, creation_date, size, path)
        self.type = "PDF"


class WebPageHTML(WebPage):
    prefix = Path.home() / Path("Documents/Archie/HTML/")

    def __init__(self, name, creation_date, size, path):
        super(WebPageHTML, self).__init__(name, creation_date, size, path)
        self.type = "HTML"
