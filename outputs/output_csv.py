import csv


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
