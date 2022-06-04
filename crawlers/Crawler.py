from utils.functions import get_cards_content


class Crawler:
    """
    Classe principal usada para gerenciar e encapsular o crawler desenvolvido.
    """

    def __init__(self):
        """
        Método inicializador do crawler.
        """
        self.data = {
            'vultr': [],
            'hostgator': []
        }
        self.urls = [
                'https://www.vultr.com/products/bare-metal/#pricing',
                'https://www.hostgator.com/vps-hosting'
        ]

    def crawler(self) -> dict:
        """
        Método responsável por realizar as operações finais da coleta do
        crawler, baseado em sua URL.

        Returns:
        Dicionário contendo todos os dados corretamente formatados e prontos
        para serem mostrados ao usuário ou armazenados.
        """
        for url in self.urls:
            if 'vultr' in url:
                self.data['vultr'] = get_cards_content(url)
            else:
                self.data['hostgator'] = get_cards_content(url)
        return self.data
