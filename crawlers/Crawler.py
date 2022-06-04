import requests

from bs4 import BeautifulSoup

from utils.functions import remove_tag, price_formatter


class Crawler:
    """
    Classe principal usada para gerenciar os crawlers desenvolvidos.
    """

    def vultr_crawler(self):
        """
        Crawler para listagem detalhada de informações das VMs oferecidas pelo
        Vultr.
        """

        content = requests.get(
            'https://www.vultr.com/products/bare-metal/#pricing').content
        html = BeautifulSoup(content, 'html.parser')
        cards = html.find_all('a', class_='package')
        crawler_data = list()
        for card in cards:
            crawler_obj = dict()
            name = card.find(class_='package__title h6').text
            raw_price = card.find(class_='price__value').text
            crawler_obj['name'] = remove_tag(name)
            crawler_obj['price'] = price_formatter(raw_price)
            body = card.find_all(class_='package__list-item')
            storage = list()
            for item in body:
                normalized_item = item.text.lower()
                if 'cores' in normalized_item:
                    crawler_obj['cpu'] = remove_tag(normalized_item)
                elif 'memory' in normalized_item:
                    crawler_obj['memory'] = remove_tag(normalized_item)
                elif 'ssd' in normalized_item or 'nvme' in normalized_item:
                    storage.append(remove_tag(normalized_item))
                    crawler_obj['storage'] = storage
                elif 'bandwidth' in normalized_item:
                    crawler_obj['bandwidth'] = remove_tag(normalized_item)
            crawler_data.append(crawler_obj)
        return crawler_data

    def hostgator_crawler(self):
        """
        Crawler para listagem detalhada de informações das VMs oferecidas pelo
        Hostgator.
        """

        ...
