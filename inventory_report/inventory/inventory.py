import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, type_report):
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
