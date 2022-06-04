import csv
import json

from pprint import pprint


def print_data(crawler_data: dict):
    """
    Retorna os dados formatados sem armazenar em disco.

    Args:
    crawler_data: dict -> Dicionário com todos os dados que devem ser printados.
    """
    pprint(crawler_data, indent=4)


def save_json(crawler_data: dict):
    """
    Salva os dados coletados num arquivo .json

    Args:
    crawler_data: dict -> Dicionário com todos os dados que devem ser gravados
    em um arquivo .json
    """
    with open('outputs/files/items.json', 'w') as json_file:
        json.dump(crawler_data, json_file, indent=4)


def save_csv(crawler_data: dict):
    """
    Salva os dados coletados num arquivo .csv

    Args:
    crawler_data: dict -> Dicionário com todos os dados que devem ser gravados
    em um arquivo .csv
    """
    headers = ['NAME', 'PRICE', 'STORAGE', 'CPU', 'MEMORY', 'BANDWIDTH']
    with open('outputs/files/items.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for key, value in crawler_data.items():
            writer.writerow([key.upper()])
            for row in value:
                writer.writerow(row.values())
