from logic.WgetWrapper import WgetWrapper
from logic.WebPage import WebPage, WebPageHTML, WebPagePDF
import pdfkit
from pathlib import Path
import datetime
import subprocess


class Archiver:
    def __init__(self):
        pass

    def download_pdf(self, name, url):
        pdfkit.from_url(url, "/home/vincent/Documents/Archie/PDF/%s"%name)
        ctime = Path("/home/vincent/Documents/Archie/PDF/%s"%name).stat().st_ctime
        webpage_datetime = datetime.datetime.fromtimestamp(ctime)
        size = Path("/home/vincent/Documents/Archie/PDF/%s"%name).stat().st_size
        size = size / 1048576
        pdf_page = WebPagePDF(name, webpage_datetime.now().date(), size, Path("/home/vincent/Documents/Archie/PDF/%s"%name))
        return pdf_page

    def download_html(self, name, url):
        warc_prefix = Path('/tmp')
        wgetter = WgetWrapper()
        wgetter.download_warc(name, warc_prefix, url)
        webpage_path = self.uncompress_warc(warc_prefix / (name + '.warc.gz'), name)
        ctime = webpage_path.stat().st_ctime
        webpage_datetime = datetime.datetime.fromtimestamp(ctime)
        size = webpage_path.stat().st_size
        size = size / 1048576
        html_page = WebPageHTML(name, webpage_datetime.now().date(), size, webpage_path)
        return html_page

    def search_by_url(self, url, file_type, name):
        new_webpage = None
        if file_type == "HTML":
            new_webpage = self.download_html(name, url)
        elif file_type == "PDF":
            new_webpage = self.download_pdf(name, url)
        print(type(new_webpage))
        return new_webpage

    def get_url_by_topic(self, topic):
        try:
            from googlesearch import search
        except ImportError:
            print("No module named 'google' found")

        for first_page in search(topic, tld="com", num=1, stop=1, pause=2):
            return str(first_page)

    def search_by_topic(self, topic, file_type, name):
        url = self.get_url_by_topic(topic)
        new_webpage = None

        if file_type == "HTML":
            new_webpage = self.download_html(name, url)
        elif file_type == "PDF":
            new_webpage = self.download_pdf(name, url)
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
