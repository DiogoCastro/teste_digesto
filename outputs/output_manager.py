import csv
import json

from pprint import pprint


def print_data(crawler_data: list):
    """
    Retorna os dados formatados sem armazenar em disco.

    Args:
    crawler_data: list -> Lista com todos os dados que devem ser printados.
    """
    pprint(crawler_data, indent=4)


def save_json(crawler_data: list):
    """
    Salva os dados coletados num arquivo .json

    Args:
    crawler_data: list -> Lista com todos os dados que devem ser gravados.
    """
    with open('outputs/files/items.json', 'w') as json_file:
        json.dump(crawler_data, json_file)


def save_csv(crawler_data: list):
    """
    Salva os dados coletados num arquivo .csv

    Args:
    crawler_data: list -> Lista com todos os dados que devem ser gravados.
    """
    keys = crawler_data[0].keys()
    headers = [key.upper() for key in keys]
    with open('outputs/files/items.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for data in crawler_data:
            writer.writerow(data.values())
