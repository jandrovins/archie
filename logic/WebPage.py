from pathlib import Path
from shutil import make_archive


class WebPage:
    def __init__(self, name, creation_date, size, path, page_type='UNKNOWN'):
        self.name = name
        self.creation_date = creation_date
        self.size = size
        self.path = path
        self.page_type = page_type

    def compress(self):
        zip_file = str(Path.home() / "Downloads" / webpage.name)
        make_archive(zip_file, "zip", webpage.path)
        


class WebPagePDF(WebPage):
    prefix = Path.home() / Path("Documents/Archie/PDF/")

    def __init__(self, name, creation_date, size, path):
        super(WebPagePDF, self).__init__()
        self.type = "PDF"


class WebPageHTML(WebPage):
    prefix = Path.home() / Path("Documents/Archie/HTML/")

    def __init__(self, name, creation_date, size, path):
        super(WebPageHTML, self).__init__()
        self.type = "HTML"
