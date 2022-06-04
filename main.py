import sys

from crawlers.Crawler import Crawler
from outputs.output_manager import print_data


if __name__ == '__main__':
    if len(sys.argv) > 1:
        crawler = Crawler()
        vultr = crawler.vultr_crawler()
        if sys.argv[1] == '--print':
            print_data(vultr)
    else:
        print(
            (
                'Por favor, insira uma das opções válidas: '
                '[--print], [--save_csv] ou [--save_json]'
            )
        )
