# Desafio Webcrawler BIT

## Configurações Iniciais

Basta apenas se certificar de que possui o _Python 3_ e seu pacote de instalação (_pip_) instalado, precisa também ter o _MongoDB_ instalado na sua máquina e instalar os pacotes que estão dentro do arquivo _"requirements.txt"_. Feito isso, tudo já estará pronto para continuar!

[Link para auxílio na instalação do MongoDB](https://docs.mongodb.com/manual/installation/)

_Para a instalação dos pacotes..._
```console
$ pip install -r requirements.txt
```


## Como Rodar

Execute o comando (dentro da pasta _quotes_project_)
```console
$ scrapy crawl quotes
```

O web crawler irá rodar, de acordo com o que está definido em _quote_spider.py_. Logo após, as informações serão salvas no banco de dados criado com o nome de _quotestoscrape_, dentro da collection _diogo_castro_, conforme definido pelo pipeline criado.

Ambos os arquivos exportados, tanto em JSON quanto em CSV estão disponíveis na pasta principal
do projeto (_quotes_project_), caso seja necessário ter uma base de como os dados estão estruturados e dispostos.

## Relatórios

Todas as queries necessárias solicitadas, com comentários explicando quais serão os retornos, estão dentro do arquivo _queries.js_. Tudo que precisa ser feito é executar esses comandos para que os resultados sejam retornados da forma esperada.
