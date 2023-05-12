from collections import Counter

from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(data):
        now = datetime.now().date()
        fac_date = [d_factory["data_de_fabricacao"] for d_factory in data]
        validities = [valid["data_de_validade"] for valid in data]
        validities_formated = [
            datetime.strptime(item, "%Y-%m-%d").date() for item in validities
        ]
        handle_validities = []
        for validity in validities_formated:
            if validity > now:
                handle_validities.append(validity)
        comp_more_p = Counter([comp["nome_da_empresa"] for comp in data])
        return f"""Data de fabricação mais antiga: {min(fac_date)}
Data de validade mais próxima: {min(handle_validities)}
Empresa com mais produtos: {comp_more_p.most_common(1)[0][0]}"""
