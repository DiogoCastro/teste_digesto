import sys

from crawlers.Crawler import Crawler
from outputs.output_manager import print_data, save_csv, save_json


if __name__ == '__main__':
    if len(sys.argv) > 1:
        crawler = Crawler()
        vultr = crawler.vultr_crawler()
        if sys.argv[1] == '--print':
            print_data(vultr)
        elif sys.argv[1] == '--save_csv':
            save_csv(vultr)
        elif sys.argv[1] == '--save_json':
            save_json(vultr)
    else:
        print(
            (
                'Por favor, insira uma das opções válidas: '
                '[--print], [--save_csv] ou [--save_json]'
            )
        )
