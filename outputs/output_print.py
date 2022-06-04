from pprint import pprint


def print_data(crawler_data: dict):
    """
    Retorna os dados formatados sem armazenar em disco.

    Args:
    crawler_data: dict -> Dicionário com todos os dados que devem ser
    mostrados.
    """
    pprint(crawler_data, indent=4)
