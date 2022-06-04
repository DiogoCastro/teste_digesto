Teste Digesto
===

Projeto criado com o intuito de mostrar meus conhecimentos de coleta usando a linguagem Python. Foi um desafio interessante, já que foi pedido para seguir sem que utilizasse a ferramenta principal e mais robusta do Python, que é o Scrapy. Mas contornei isso utilizando as bibliotecas `requests` e `BeautifulSoup`, que, apesar de mais simples, ainda proporcionaram a possibilidade de fazer a coleta da mesma forma, no fim das contas, apenas usando alguns passos a mais.

## Pré-requisitos
- `python >= 3.8.0`

## Instalação
Para instalar as bibliotecas necessárias é muito simples. Basta executar o comando abaixo no seu terminal:
- `pip install -r requirements.txt`
Feito isso, basta apenas esperar, que todos os pacotes serão instalados automaticamente.

## Executando o script
Para executar também é extremamente simples, basta usar um dos comandos abaixo, de acordo com sua preferência de visualização/armazenamento dos dados coletados no crawler, que poderão ser mostrados/armazenados de 3 formas diferentes:

- `python main.py --print`
Mostra os dados diretamente no seu terminal, permitindo uma visualização instantânea.
- `python main.py --save_json`
Salva os dados coletados diretamente em um arquivo .json
- `python main.py --save_csv`
Salva os dados coletados diretamente em um arquivo .csv

## Visualizando os resultados
Dentro do repositório temos os arquivos formatados e já salvos, caso necessário, os arquivos com os resultados finais podem ser encontrados no diretório `outputs/files`.
> Esse também é o diretório responsável por abrigar os arquivos que são gerados quando o script é executado.

## Problem Solving
Como dito anteriormente, um dos desafios propostos foi de utilizar uma biblioteca menor para a coleta dos dados dos websites, então decidi me inspirar um pouco na estrutura de crawlers que criamos na empresa que trabalho atualmente. Como poderão ver, eu apliquei ao máximo que pude os conceitos DRY (Don't Repeat Yourself) e também segui com as principais propostas da PEP8, para manter uma boa legibilidade por parte de quem for analizar o código. Caso necessário também, cada uma das funções que criei estão com docstrings explicando em resumo o que fazem e os parâmetros que devem ser utilizados ou até mesmo o tipo de dado que será retornado.

#### Crawlers
Como pode ser visto no arquivo `crawlers/Crawler.py`, ambos os crawlers compartilham uma mesma função que é usada para popular seus valores baseados na url que, por sua vez, é definida a partir de uma lista gerada na inicialização da classe. Escolhi fazer dessa forma justamente para evitar de ficar repetindo linhas de código desnecessárias, o que causaria um grande desconforto de se olhar e avaliar. Afinal, segundo o Zen of Python:

> Simple is better than complex
--
E, durante o desenvolvimento desse projeto tive muito isso em mente.

#### Functions
Em relação ao que desenvolvi no arquivo `utils/functions.py`:
Quando desenvolvo algo eu sempre prefiro separar as funções utilitarias para caso precise mexer em algo já saber exatamente onde precisarei focar. E esse projeto não foi diferente, ter criado esse arquivo me permitiu ter um ganho de tempo muito grande, já que me mantive 100% do tempo organizado e com plena noção de onde estava cada funcionalidade que eu precisaria desenvolver ou corrigir.
Aqui, como podemos ver, eu criei a função responsável por fazer a coleta dos dados baseados na URL do website. Como a estrutura era bastante parecida no fim das contas, eu precisei apenas dividir em duas funções, onde uma (`get_body_value`) apenas pegava os dados do "corpo" dos cards com as informações, e a função mãe (`get_cards_content`) permitia que esses dados fossem estruturados e formatados corretamente. Assim acabei conseguindo quebrar uma função que teria muitas linhas de código repetidas para então transformar em duas que se completavam.
Dentro desse arquivo também criei mais duas funções responsáveis por "limpar" os dados retornados:
- A função `remove_tag`, que eu criei para poder remover e normalizar as strings que estavam sendo retornadas por meio do BeautifulSoup, já que muitas das vezes só era possível pegar algum dado vindo diretamente com a tag.
- A função `price_formatter`, que eu criei levando em consideração o formato do preço em ambos os websites. Nessa função eu usei um regex bem simples para poder substituir qualquer caractere que não seja um dígito ou um ponto literal. Assim temos uma solução simples e concisa para resolver o caso de que em um site o preço é mostrado separado por ponto e o outro é mostrado formatado no valor completo, mas utilizando vírgula.
>Uma coisa interessante de ressaltar em relação aos preços é que dentro da URL do Vultr temos apenas 10 itens com preços explícitos na tela, os 2 últimos é apenas entrando em contato diretamente com eles. E essa função também se encarrega de validar isso, ou seja, caso não tenha nenhum preço sendo mostrado, o valor retornado ao usuário será nulo. Caso isso não fosse tratado poderia haver inconsistências na hora de retornar o valor, até mesmo causando erros indesejados.

#### Outputs
Em relação aos outputs a ideia foi bem básica. Decidi criar todas as funções usando apenas bibliotecas padrão do Python, já que é mais do que o suficiente para esses casos. Então eu criei um gerenciador de opções que podem ser chamadas por meio do console, e cada uma dessas opções era responsável por executar uma função específica:
- `print_data`: Essa é a mais simples de todas, optei por usar uma lib padrão do Python chamada pprint para que os dados fossem mostrados de uma forma mais agradável e organizada no console.
- `save_json`: Outra função bem padrão também. Usei a lib padrão do Python chamada json, e a partir dela eu chamei o método dump para que me permitisse salvar os dados diretamente no arquivo que passei como argumento desse método.
- `save_csv`: Função criada para armazenar os itens em formato de planiha (csv). Aqui eu preferi definir uma lista com todos os headers da forma que foram pedidos no teste. Então, tendo esses headers separados, a única coisa que precisei fazer foi iterar nos dados retornados, pegando primeiro as chaves que continham o nome do site sendo crawleado e passando esse valor para maiúsculo, para se manter no padrão dos headers. Então depois eu apenas peguei os valores dentro de cada um dos crawlers e inseri as linhas no arquivo csv.


## Finalizando
> Espero que as explicações e minha forma de pensar tenham ficado claras para vocês! Eu gostaria de agradecer muito pela oportunidade e espero que tenham gostado da forma que arrumei para pensar e solucionar os problemas propostos. Como eu já havia dito, foi um projeto bem interessante, porque me tirou da zona de conforto e permitiu que eu achasse novas formas de solucionar problemas que eu já resolvia em poucos minutos utilizando o Scrapy.
Espero poder contribuir com vocês em breve!
