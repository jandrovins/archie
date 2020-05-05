from WgetWrapper import WgetWrapper
import pdfkit
from pathlib import Path

class Archiver:

    def __init__(self):
        pass

    def download_pdf(self, warc_file, prefix, url):
        wgetter = WgetWrapper()
        wgetter.download_warc(warc_file, prefix, url)
        self.uncompress_warc(prefix)
        pdfkit.from_file('%s/%s.html'%(prefix, warc_file),'%s.pdf'%name)
        
    def download_html(self, warc_file, prefix, url):
        wgetter = WgetWrapper()
        wgetter.download_warc(warc_file, prefix, url)
        self.uncompress_warc(prefix)
