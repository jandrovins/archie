from WgetWrapper import WgetWrapper
import pdfkit
from pathlib import Path
import datetime

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
