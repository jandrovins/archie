import subprocess
import pathlib

class WgetWrapper:
    
    #Empty consrtuctor
    def __init__(self):
        pass
        
    #download_warc method downloads the compressed warc file and then moves it to the defined directory
    @staticmethod
    def download_warc(warc_file, prefix, url):
        subprocess.run(['wget', url, '--warc-file=%s'% warc_file, '-P%s'% str(prefix)])
        subprocess.run(['mv', '%s.warc.gz'% warc_file, str(prefix)])

