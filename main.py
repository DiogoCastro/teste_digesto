from crawlers.Crawler import Crawler
from outputs.output_manager import set_options


if __name__ == '__main__':
    crawler = Crawler()
    crawler_runner = crawler.crawler()
    set_options(crawler_runner)
