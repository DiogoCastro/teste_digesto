import re

import requests

from bs4 import BeautifulSoup
from cleantext import clean


def get_cards_content(url: str) -> list:
    """
    Captura o conteúdo dos cards para cada VM baseado em sua URL especificada.

    Args:
    url: str -> URL que deve ser passada para realizar as operações

    Returns:
    Uma lista contendo todos os dados já formatados prontos para serem usados.
    """
    content = requests.get(url).content
    html = BeautifulSoup(content, 'html.parser')
    crawler_data = []
    if 'vultr' in url:
        cards = html.find_all('a', class_='package')
        for card in cards:
            crawler_obj = dict()
            name = card.find(class_='package__title h6').text
            raw_price = card.find(class_='price__value').text
            crawler_obj['name'] = remove_tag(name)
            crawler_obj['price'] = price_formatter(raw_price)
            body = card.find_all(class_='package__list-item')
            crawler_obj.update(get_body_value(body))
            crawler_data.append(crawler_obj)
    else:
        cards = html.find_all('div', class_='pricing-card')
        for card in cards:
            crawler_obj = dict()
            name = card.find(class_='pricing-card-title').text
            raw_price = card.find(class_='pricing-card-price').text
            crawler_obj['name'] = remove_tag(name)
            crawler_obj['price'] = price_formatter(raw_price)
            body = card.find_all(class_='pricing-card-list-items')
            crawler_obj.update(get_body_value(body))
            crawler_data.append(crawler_obj)
    return crawler_data


def get_body_value(body: list) -> dict:
    """
    Realiza as operações necessárias atribuindo os valores corretos baseados
    nos dados referentes ao corpo do card.

    Args:
    body: list -> A lista com os valores a serem processados.

    Returns:
    Dicionário com os valores a serem usados para concluir a coleta do crawler.
    """
    crawler_obj = dict()
    storage = list()
    for item in body:
        normalized_item = item.text.lower()
        if 'core' in normalized_item:
            crawler_obj['cpu'] = remove_tag(normalized_item)
        elif 'memory' in normalized_item or 'ram' in normalized_item:
            crawler_obj['memory'] = remove_tag(normalized_item)
        elif 'ssd' in normalized_item or 'nvme' in normalized_item:
            storage.append(remove_tag(normalized_item))
            crawler_obj['storage'] = storage
        elif 'bandwidth' in normalized_item:
            crawler_obj['bandwidth'] = remove_tag(normalized_item)
    return crawler_obj


def remove_tag(html_text: str) -> str:
    """
    Remove a tag HTML dado o texto html passado por parâmetro.

    Args:
    html_text: str -> Texto HTML em questão.

    Returns:
    Retorna string já formatada e sem as tags.
    """
    if html_text:
        rm_tag_pattern = re.compile(r'<.*?>')
        clean_html = clean(
            re.sub(rm_tag_pattern, '', html_text), no_line_breaks=True)
        return clean_html


def price_formatter(raw_price: str):
    """
    Formata o preço que é recuperado em formato de string.

    Args:
    raw_price: str -> Preço "raw" a ser formatado.

    Returns:
    Retorna o preço formatado no tipo float, caso seu tamanho seja maior que 0,
    senão, retorna um valor nulo.
    """
    fmt_price = re.sub(r'[^\.|\d]', '', raw_price)
    if len(fmt_price) > 0:
        return float(fmt_price)
    return None
