import logging
import sys

from outputs.output_json import save_json
from outputs.output_csv import save_csv
from outputs.output_print import print_data

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


def set_options(crawler_runner: dict):
    options = [
        '--print',
        '--save_csv',
        '--save_json',
    ]
    try:
        if sys.argv[1] == options[0]:
            print_data(crawler_runner)
        elif sys.argv[1] == options[1]:
            save_csv(crawler_runner)
        elif sys.argv[1] == options[2]:
            save_json(crawler_runner)
    except IndexError:
        logging.error(
                f'Por favor, insira uma das opções válidas: {options}'
        )
