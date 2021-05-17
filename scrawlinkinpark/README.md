>_Scrawling in my scheme_
_These quotes, they will not yield..._

# Desafio Webcrawler BIT

## Requisitos Funcionais

1. Construir um web crawler com o _framework_ [Scrapy](https://scrapy.org/).
2. Coletar as citações na página _http://quotes.toscrape.com_.
3. Armazenar citação (string), autor (dicionário) com nome (string) e url da bio (string) e _tags_ (array) numa base de dados _MongoDB_.
4. Responder, através de _queries_ no _MongoDB_:
   - Quantas citações foram coletadas?
   - Quantas tags distintas foram coletadas?
   - Quantas citações por autor foram coletadas? _(exemplo abaixo)_

![](https://github.com/b2w-atech/desafio-webcrawler/raw/master/mongodb_aggregate.png)

## Requisitos Não-Funcionais

1. Construir um crawler robusto, ágil e resistente a mudanças da matriz tecnológica.
2. Estruturar os componentes de forma coesa, sem lhes comprometer com acoplamento excessivo.
3. Manter uma documentação em código concisa, legível e cuidadosa.

## Instalação

Embora não haja um impeditivo imperativo sobre o uso da instalação global, o uso de um ambiente virtual Python é extremamente encorajado. O mecanismo mais adequado é o [Pipenv](https://pipenv.pypa.io/en/latest/install/), através do comando `pipenv shell && pipenv install`, que o criará e instalará todas as dependências (exceto o _MongoDB_) automaticamente. Também é possível usar o `pip3` através do comando `pip3 install -r `[`requirements.txt`](../requirements.txt). Apenas certifique-se de que a versão do Python é compatível.

## Execução

Usando a versão 2.5.0 do [Scrapy](https://scrapy.org/) sobre [Python 3.9.5](https://www.python.org/downloads/release/python-395/) e ao lado do [MongoDB 4.4.2](https://docs.mongodb.com/manual/installation/), um _pipeline_ simplificado foi construído para raspar o site de citações e armazená-las num banco de dados de nome `quotestoscrape`, sob coleção denominada `ramon_melo`. O robô armazena o texto da citação como uma string; o autor como um dicionário de chaves `name` e `url`; e as etiquetas numa lista encadeada.

As consultas de teste estão gravadas em [`queries.js`](queries.js). Os resultados foram obtidos através do comando:

> [`scrawlinkinpark/scrawlinkinpark/spiders`](scrawlinkinpark/spiders/quotes_spyder.py)`$  scrapy runspider quotes_spyder.py -O `[`../../../tests/quotes.json`](../tests/quotes.json)


É importante observar com atenção o diretório onde o programa é executado. Ele grava os resultados sequencial e similarmente no arquivo [`tests/quotes.json`](../tests/quotes.json) e no banco de dados localizado no endereço padrão `mongodb://127.0.0.1:27017`, permitindo uma comparação direta e até automatizada dos mesmos. Caso outro endereço seja utilizado, é importante modificar a variável `MONGO_URI` ao final do arquivo [`settings.py`](scrawlinkinpark/settings.py). Utilizando a ferramenta _MongoDB Shell_ e execuções sucessivas, foi observada total concordância entre ambos.

O comando acima inclui, ainda, a possibilidade de varrer somente uma categoria do site, passando o parâmetro `-a tag=CATEGORIA`. As configurações incluem, também, customizações específicas de privacidade para o robô, já que é comum que sites tentem impedir a varredura quando notado. O programa tem a capacidade de circular entre diferentes configurações de strings de _user-agent_, cabeçalhos de navegadores comuns e, por fim, de retornar à configuração padrão.

## Dependências

- [Python 3.9](https://www.python.org/downloads/release/python-395/)
- [Scrapy 2.5](https://scrapy.org/)
- [MongoDB 4.4](https://docs.mongodb.com/manual/installation/)
- [PyMongo 3.11](https://pymongo.readthedocs.io/en/stable/installation.html)
- [Attrs 21.2](https://www.attrs.org/en/stable/index.html#getting-started) (melhoria de legibilidade)
- [scrapy-fake-useragent](https://github.com/alecxe/scrapy-fake-useragent) (privacidade)

## Conclusão

O projeto foi uma oportunidade bem aproveitada de usar um domingo frio para aquecer minhas engrenagens e praticar uma _reciclagem_. Agradeço desde já o desafio e toda a atenção dispensada.

>_This spyder endlessly has pulled the Web upon me_
_Distracting... Overwriting..._
