from pathlib import Path
from shutil import make_archive
from datetime import date
import WebPage


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
        creation_date_str = webpage.date.strftime("%Y-%m-%d")
        page_type = webpage.type
        line = f"{name},{abs_path},{size},{creation_date_str},{page_type}\n"
        with csv_path.open("w") as csv:
            csv.write(line)

    @classmethod
    def parse_csv(cls):
        with cls.csv_path.open() as csv:
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
                year = creation_date_obj_list[0]
                month = creation_date_obj_list[1]
                day = creation_date_obj_list[2]
                creation_date = date(year, month, day)
                page_type = values[4]

                # Create WebPage and add it to FileManager web pages list
                cls.webpages.append(
                    WebPage(name, abs_path, size, creation_date, page_type)
                )

    @classmethod
    def list_web_pages(cls):
        return cls.webpages
    
    @classmethod
    def compress(cls, webpage):
        zip_file = (Path.home() / 'Downloads' / webpage.name).__str__()
        make_archive(zip_file, 'zip', webpage.path)
