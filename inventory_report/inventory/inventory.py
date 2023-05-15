import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

# from inventory_report.importer.csv_importer import CSVImporter
# from inventory_report.importer.json_importer import JSONImporter
# from inventory_report.importer.xml_importer import XMLImporter


class Inventory:
    @staticmethod
    def relatorio_csv(path, type_report):
        with open(path, encoding="utf-8") as file:
            inventory_reader = csv.DictReader(
                file, delimiter=",", quotechar='"'
            )
            all_items = []
            for item in inventory_reader:
                all_items.append(item)
        if type_report == "simples":
            return SimpleReport.generate(all_items)
        elif type_report == "completo":
            return CompleteReport.generate(all_items)

    @staticmethod
    def relatorio_json(path, type_report):
        with open(path) as file:
            all_items = json.load(file)
        if type_report == "simples":
            return SimpleReport.generate(all_items)
        elif type_report == "completo":
            return CompleteReport.generate(all_items)

    @staticmethod
    def relatorio_xml(path, type_report):
        with open(path) as file:
            file_reader = file.read()
        all_items = xmltodict.parse(file_reader)
        if type_report == "simples":
            return SimpleReport.generate(all_items["dataset"]["record"])
        elif type_report == "completo":
            return CompleteReport.generate(all_items["dataset"]["record"])

    @staticmethod
    def import_data(path, type_report):
        if path.endswith(".csv"):
            return Inventory.relatorio_csv(path, type_report)
        if path.endswith(".json"):
            return Inventory.relatorio_json(path, type_report)
        if path.endswith(".xml"):
            return Inventory.relatorio_xml(path, type_report)


# class Inventory:
#     def __init__(self, __file_importer):
#         __file_importer = __file_importer

#     def import_data(self, path, type_report):
#         if type_report == "simples":
#             return SimpleReport.generate(self.__file_importer(path))
#         elif type_report == "completo":
#             return CompleteReport.generate(self.__file_importer(path))
