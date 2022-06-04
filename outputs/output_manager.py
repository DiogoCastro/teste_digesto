import logging
import sys

from outputs.output_json import save_json
from outputs.output_csv import save_csv
from outputs.output_print import print_data

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


def set_options(crawler_runner: dict):
    """
    Cria opções que permitem ser executadas a partir da chamada de um arquivo
    no console.

    Args:
    crawler_runner: dict -> Dicionário com todas as informações que devem ser
    passadas para a função que se encarregará de mostrar os dados na tela ou
    salvar os dados no disco, a partir do formato escolhido.
    """
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
