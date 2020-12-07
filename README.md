# Desafio Webcrawler BIT

## Sobre

O desafio consiste na implementação de um _crawler_ que colete citações do site _http://quotes.toscrape.com_.

## Regras

Utilizando o _framework_ [Scrapy](https://scrapy.org/), desenvolva uma robô que visite o [site](http://quotes.toscrape.com) citado anteriormente e colete todas as citações exibidas nas páginas.

### Premissas:
1. Para cada citação, os seguintes dados devem ser coletados: citação (string), autor (dictionary) com seu nome(string) e url da sua bio (string) e _tags_ (array).
2. As citações devem ser salvas em um arquivo _json_.
3. Deve utilizar o [_pipeline_](https://docs.scrapy.org/en/latest/topics/item-pipeline.html#write-items-to-a-json-file) do _Scrapy_ para salvar cada item no arquivo _json_.
4. Enquanto houver paginação, o _crawler_ deve continuar coletando os dados.
5. Ao final, um arquivo _json_ deve armazenar todos os items coletados.

## Recomendações:
- Utilize a versão mais recente do Python (https://www.python.org/)
- Leia a documentação do [Scrapy](https://scrapy.org/) e faça o exemplo inicial para se familiarizar com o _framework_.
- Atente-se aos tipos de dados exigidos para cada campo.

## Exemplo de inserção no _json_
Cada citação deve ser salva no arquivo _json_ seguindo o seguinte formato:

![](https://github.com/b2w-atech/desafio-webcrawler/raw/master/quote_albert_einstein.png)

```json
{
  "text": "\u201cThe world as we have created it is a process of our thinking. It cannot be changed without changing our thinking\u201d",
  "author": {
    "name": "Albert Einstein",
    "url": "http://quotes.toscrape.com/author/Albert-Einstein"
  },
  "tags": [
      "change",
      "deep-thoughts",
      "thinking",
      "world"
    ]
  }
```

## ...

Tudo pronto? Basta clonar esse repositório e abrir um **pull request** quando finalizar ;)
