# Desafio Webcrawler BIT

## Sobre

O desafio consiste na implementação de um _crawler_ que colete e armazene citações do site _http://quotes.toscrape.com_.

## Regras

Utilizando o _framework_ [Scrapy](https://scrapy.org/), desenvolva uma robô que visite o [site](http://quotes.toscrape.com) citado anteriormente, colete todas as citações exibidas nas páginas e armazene no _MongoDB_.

### Premissas:
1. Para cada citação, os seguintes dados devem ser coletados: citação (string), autor (dictionary) com seu nome(string) e url da sua bio (string) e _tags_ (array).
2. Deve utilizar o [_pipeline_](https://docs.scrapy.org/en/latest/topics/item-pipeline.html#write-items-to-a-json-file) do _Scrapy_ para salvar cada item no banco de dados.
3. Enquanto houver paginação, o _crawler_ deve continuar coletando e armazenando os dados.
4. No final, os dados devem estar armazenados no _MongoDB_ no banco de dados _quotestoscrape_ e na collection _seunome_seusobrenome_.

### Relatórios
As seguintes perguntas devem ser respondidas através de _queries_ no _MongoDB_:

- Quantas citações foram coletadas?
- Quantas tags distintas foram coletadas?
- Quantas citações por autor foram coletadas? _(exemplo abaixo)_

![](https://github.com/b2w-atech/desafio-webcrawler/raw/master/mongodb_aggregate.png)

_Obs.: Salve suas queries em .js e envie-as junto do projeto no github._

## Recomendações:
- Utilize a versão mais recente do Python (https://www.python.org/)
- Leia a documentação do [Scrapy](https://scrapy.org/) e faça o exemplo inicial para se familiarizar com o _framework_.
- Leia sobre [agregações](https://docs.mongodb.com/manual/aggregation/) no MongoDB.
- Atente-se aos tipos de dados exigidos para cada campo.

## Exemplo de uma citação a ser inserida no banco de dados
Cada citação deve ser salva no _MongoDB_ seguindo o seguinte formato:

![](https://github.com/b2w-atech/desafio-webcrawler/raw/master/quote_albert_einstein.png)

```json
{
    "_id" : ObjectId("5fcf74d9439554bbdaf8da5d"),
    "title" : "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”",
    "author" : {
        "name" : "Albert Einstein",
        "url" : "http://quotes.toscrape.com//author/Albert-Einstein"
    },
    "tags" : [ 
        "change", 
        "deep-thoughts", 
        "thinking", 
        "world"
    ]
}
```

## ...

Tudo pronto? Basta criar um _fork_ deste repositório e abrir um **pull request** quando finalizar ;)

Em caso de dúvidas, envie um e-mail pra gente: analytics.tech@b2wdigital.com 
