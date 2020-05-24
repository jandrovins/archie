from logic.WgetWrapper import WgetWrapper
from logic.WebPage import WebPage, WebPageHTML, WebPagePDF
import pdfkit
from pathlib import Path
import datetime
import subprocess
from abc import ABC, abstractmethod

class Archiver(ABC):
    def __init__(self):
        pass

    #path is a Path pathlib object
    def get_size(self, path):
        size = path.stat().st_size
        size = size / 1048576
        return size
    
    def get_ctime(self, path):
        creation_time = path.stat().st_ctime
        webpage_datetime = datetime.datetime.fromtimestamp(creation_time)
        ctime = webpage_datetime.now().date()
        return ctime

    #prefix is a Path pathlib object
    def download_pdf(self, prefix, name, url):
        file_dir = prefix / 'PDF' / name
        file_dir.mkdir()
        file_path = file_dir / f'{name}.pdf'
        pdfkit.from_url(url, str(file_path))
        pdf_page = WebPagePDF(name, self.get_ctime(file_path), self.get_size(file_path), file_path)
        return pdf_page

    def download_html(self, name, url):
        warc_prefix = Path('/tmp')
        wgetter = WgetWrapper(name, warc_prefix, url)
        wgetter.download_warc()
        webpage_path = self.uncompress_warc(warc_prefix / (name + '.warc.gz'), name)
        html_page = WebPageHTML(name, self.get_ctime(webpage_path), self.get_size(webpage_path), webpage_path)
        return html_page

    def search_by_url(self, url, file_type, name, prefix):
        new_webpage = None
        if file_type == "HTML":
            new_webpage = self.download_html(name, url)
        elif file_type == "PDF":
            new_webpage = self.download_pdf(prefix, name, url)
        return new_webpage

    def get_url_by_topic(self, topic):
        try:
            from googlesearch import search
        except ImportError:
            print("No module named 'google' found")

        for first_page in search(topic, tld="com", num=1, stop=1, pause=2):
            return str(first_page)

    def search_by_topic(self, topic, file_type, name, prefix):
        url = self.get_url_by_topic(topic)
        new_webpage = None

        if file_type == "HTML":
            new_webpage = self.download_html(name, url)
        elif file_type == "PDF":
            new_webpage = self.download_pdf(prefix, name, url)
        return new_webpage

    def uncompress_warc(self, path, name):
        home = Path.home()
        page_name = name + "/"
        destination = home / Path("Documents/Archie/HTML/") / Path(page_name)
        uncompress_warc = subprocess.Popen(
            [
                "python",
                "-m",
                "warcat",
                "extract",
                str(path),
                "--output-dir",
                str(destination),
                "--progress",
            ]
        )
        uncompress_warc.wait()
        uncompress_warc.poll()
        return destination

