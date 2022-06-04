import json


def save_json(crawler_data: dict):
    """
    Salva os dados coletados num arquivo .json

    Args:
    crawler_data: dict -> Dicionário com todos os dados que devem ser gravados
    em um arquivo .json
    """
    with open('outputs/files/items.json', 'w') as json_file:
        json.dump(crawler_data, json_file, indent=4)
