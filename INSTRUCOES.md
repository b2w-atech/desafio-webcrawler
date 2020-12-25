# Desafio Webcrawler BIT

## Configurações iniciais:

- Certificar de que possui o python 3.
- O MongoDB estou utilizando o MongoDB Atlas que é em nuvem, portanto, o link para poder utiilzar via Shell/MongoDB
  Compass ou alguma IDE que permita que faça consultas em banco é esse: <br>
  ``mongodb+srv://admin:<password>@cluster0.lw17c.mongodb.net/<dbname>?retryWrites=true&w=majority
  `` <br>
  OBS: Trocar as tags `<password>` e `<dbname>` para conseguir ter plena utilização do banco de dados.

- Caso ainda não tenha o PyMongo, DNSPython ou o Scrapy, na pasta raíz tem o arquivo `requirements.txt` que irá fazer a
  instalação dos pacotes principais para rodar o robô. No CMD você pode digitar: <br>
  ``pip install -r requirements.txt``

## Como rodar:

Entrar na pasta WebCrawling/spiders e executar o comando no CMD:<br>
``scrapy crawl quotes``

O robô irá fazer a varredura de todas as citações — página por página — e irá guardar esses dados no banco `quotescrape`
na collection `marcosvinicius_simoescampos`.

## Queries:

Todas as queries que foram pedidas estão no arquivo `queries.js`. Lá tem os comentários sobre o retorno esperado. Tudo
que precisa ser feito é copiar e colar na ferramenta de consulta para verificar os dados que foram estruturados conforme
foi solicitado.

#### OBS: O arquivo ``items.json`` que está na pasta raíz foi criado para que veja como está estruturado os dados.