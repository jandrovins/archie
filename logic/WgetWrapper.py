import subprocess
import pathlib

class WgetWrapper:
    warc_file = None
    prefix = None
    url = None
    
    #Empty consrtuctor
    def __init__(self, warc_file, prefix, url):
        self.warc_file = warc_file
        self.prefix = prefix
        self.url = url
        
    #download_warc method downloads the compressed warc file and then moves it to the defined directory
    def download_warc(self):
        subprocess.run(['wget', self.url, '--warc-file=%s'% self.warc_file, '-P%s'% str(self.prefix)])
        subprocess.run(['mv', '%s.warc.gz'% self.warc_file, str(self.prefix)])

