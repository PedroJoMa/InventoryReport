from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(path, encoding="utf-8") as file:
            inventory_reader = csv.DictReader(
                file, delimiter=",", quotechar='"'
            )
            all_items = []
            for item in inventory_reader:
                all_items.append(item)
        return all_items
