import re

from cleantext import clean


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
    fmt_price = re.sub(r'(\D)', '', raw_price)
    if len(fmt_price) > 0:
        return float(fmt_price)
    return None
