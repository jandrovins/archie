from pathlib import Path
from shutil import make_archive


class WebPage:
    def __init__(self, name, creation_date, size, path, page_type='UNKNOWN'):
        self.name = name
        self.creation_date = creation_date
        self.size = size
        self.path = path
        self.type = page_type

    def compress(self):
        zip_file = str(Path.home() / "Downloads" / self.name)
        if self.type == 'PDF':
            p = '/'.join(str(self.path).split('/')[:-1])
            make_archive(zip_file, "zip", p)
            return

        make_archive(zip_file, "zip", self.path)
        


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
