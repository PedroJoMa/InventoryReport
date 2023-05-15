from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            file_reader = file.read()
            all_items = xmltodict.parse(file_reader)
        return all_items["dataset"]["record"]
