import subprocess
from pathlib import Path

class Archie:
    def get_url_by_topic(self, topic):
        try: 
            from googlesearch import search 
        except ImportError:  
            print("No module named 'google' found")
            
        for first_page in search(topic, tld="com", num=1, stop=1, pause=2):
            return str(first_page)

    def search_by_topic(self, topic, type):
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
        
