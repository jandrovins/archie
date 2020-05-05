from pathlib import Path
from shutil import make_archive
from datetime import date
from WebPage import WebPageHTML, WebPagePDF


class FileManager:
    directory = Path.home() / "Documents/Archie"
    csv_path = directory / "webpages.csv"
    webpages = []

    @classmethod
    def add_webpage(cls, webpage):
        cls.webpages.append(webpage)
        cls.add_webpage_to_csv(webpage)

    @classmethod
    def add_webpage_to_csv(cls, webpage):
        name = webpage.name
        abs_path = str(webpage.path)
        size = str(webpage.size)
        creation_date_str = webpage.creation_date.strftime("%Y-%m-%d")
        page_type = webpage.type
        line = f"{name},{abs_path},{size},{creation_date_str},{page_type}\n"
        with cls.csv_path.open("a") as csv:
            csv.write(line)

    @classmethod
    def parse_csv(cls):
        with cls.csv_path.open('r') as csv:
            # Iterate all lines, except header
            for line in csv.readlines()[1:]:
                # Remove trailing EOL and spaces
                line = line.rstrip("\n ")
                values = line.split(",")

                # Get instance attributes
                name = values[0]
                abs_path = Path(values[1])
                size = float(values[2])
                creation_date_obj_list = values[3].split("-")
                year = int(creation_date_obj_list[0])
                month = int(creation_date_obj_list[1])
                day = int(creation_date_obj_list[2])
                creation_date = date(year, month, day)
                page_type = values[4]

                # Create WebPage and add it to FileManager web pages list
                if page_type == 'HTML':
                    cls.webpages.append(
                        WebPageHTML(name, creation_date, size, abs_path)
                    )
                else:
                    cls.webpages.append(
                        WebPagePDF(name, creation_date, size, abs_path)
                    )

    @classmethod
    def list_web_pages(cls):
        return cls.webpages

    @classmethod
    def compress(cls, webpage):
        zip_file = str(Path.home() / "Downloads" / webpage.name)
        make_archive(zip_file, "zip", webpage.path)
