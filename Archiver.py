from WgetWrapper import WgetWrapper
import pdfkit
from pathlib import Path
import datetime
import subprocess

class Archiver:

    def __init__(self):
        pass

    def download_pdf(self, warc_file, prefix, url):
        wgetter = WgetWrapper()
        wgetter.download_warc(warc_file, prefix, url)
        self.uncompress_warc(prefix)
        pdfkit.from_file('%s/%s.html'%(prefix, warc_file),'%s.pdf'%name)
        ctime = Path('/Users/IsabelPiedrahita/Workspace/archi_storage/hola.warc.gz').stat().st_ctime
        timestamp_str = datetime.datetime.fromtimestamp(mtime).strftime('%d')
        size = Path('/Users/IsabelPiedrahita/Workspace/archi_storage/hola.warc.gz').stat().st_size
        pdf_page = WebPagePDF(warc_file, timestamp_str, size, prefix)
        
    def download_html(self, warc_file, prefix, url):
        wgetter = WgetWrapper()
        wgetter.download_warc(warc_file, prefix, url)
        self.uncompress_warc(prefix)
        ctime = Path('/Users/IsabelPiedrahita/Workspace/archi_storage/hola.warc.gz').stat().st_ctime
        timestamp_str = datetime.datetime.fromtimestamp(mtime).strftime('%d')
        size = Path('/Users/IsabelPiedrahita/Workspace/archi_storage/hola.warc.gz').stat().st_size
        html_page = WebPageHTML(warc_file, timestamp_str, size, prefix)

    def search_by_url(self, url, type, name):
        if type == 'HTML':
            self.download_html(url)
        elif type == 'PDF':
            self.download_pdf(url)
        
    def get_url_by_topic(self, topic):
        try: 
            from googlesearch import search 
        except ImportError:  
            print("No module named 'google' found")
            
        for first_page in search(topic, tld="com", num=1, stop=1, pause=2):
            return str(first_page)

    def search_by_topic(self, topic, type, name):
        url = self.get_url_by_topic(topic)
        
        if type == 'HTML':
            self.download_html(url)
        elif type == 'PDF':
            self.download_pdf(url)

    def uncompress_warc(self, path, name):
        home = Path.home()
        page_name = name + "/"
        destination = home / Path("Documents/Archie/HTML/") / Path(page_name)
        uncompress_warc = subprocess.Popen(['python', '-m', 'warcat', 'extract', str(path), '--output-dir', str(destination), '--progress' ])
        uncompress_warc.wait()
        uncompress_warc.poll()

