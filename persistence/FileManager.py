from pathlib import Path
from shutil import make_archive
from datetime import date
from logic.WebPage import WebPageHTML, WebPagePDF


class FileManager:
    directory = Path.home() / "Documents/Archie"
    csv_path = directory / "webpages.csv"

    @classmethod
    def persist_webpage(cls, name, abs_path, size, creation_date, page_type):
        abs_path = str(webpage.path)
        size = str(webpage.size)
        creation_date_str = creation_date.strftime("%Y-%m-%d")
        line = f"{name},{abs_path},{size},{creation_date_str},{page_type}\n"
        with cls.csv_path.open("a") as csv:
            csv.write(line)

    @classmethod
    def parse_csv(cls):
        webpages = []
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
                webpages.append(
                        (name, creation_date, size, abs_path, page_type)
                        )
        return webpages
