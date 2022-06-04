from pprint import pprint


def print_data(crawler_data: list):
    """
    Retorna os dados formatados sem armazenar em disco.

    Args:
    crawler_data: str -> Lista com todos os dados que devem ser printados.
    """
    pprint(crawler_data, indent=4)
