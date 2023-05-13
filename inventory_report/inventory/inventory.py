import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


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
    def import_data(path, type_report):
        if path.endswith(".csv"):
            return Inventory.relatorio_csv(path, type_report)
        if path.endswith(".json"):
            return Inventory.relatorio_json(path, type_report)
