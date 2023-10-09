import re


def is_a_valid_cnpj(cnpj: str):
    cnpj_numbers = re.sub(r"[^\d]", "", cnpj)
    return len(cnpj_numbers) == 14
