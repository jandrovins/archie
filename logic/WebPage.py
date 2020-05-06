from abc import ABC, abstractmethod
from pathlib import Path
import shutil

class WebPage(ABC):
    @abstractmethod
    def __init__(self, name, creation_date, size, path):
        pass


class WebPagePDF(WebPage):
    prefix = Path.home() / Path("Documents/Archie/PDF/")

    def __init__(self, name, creation_date, size, path):
        self.name = name
        self.creation_date = creation_date
        self.size = size
        self.path = path
        self.type = 'PDF'
    

class WebPageHTML(WebPage):
    prefix = Path.home() / Path("Documents/Archie/HTML/")

    def __init__(self, name, creation_date, size, path):
        self.name = name
        self.creation_date = creation_date
        self.size = size
        self.path = path
        self.type = 'HTML'
