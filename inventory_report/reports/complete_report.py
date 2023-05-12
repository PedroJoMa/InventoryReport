from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(data):
        report = SimpleReport.generate(data)
        companies_quantity = Counter(
            [company["nome_da_empresa"] for company in data]
        )
        report += "\nProdutos estocados por empresa:\n"
        for name, quantity in companies_quantity.items():
            report += f"- {name}: {quantity}\n"
        return report
