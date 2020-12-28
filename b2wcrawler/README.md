# Webcrawler

O robô, localizado em `b2crawler/spiders`, faz a varredura de todas as páginas do website *http://quotes.toscrape.com/*.  
O formato dos registros segue o modelo indicado, e a pipeline faz o registro dos itens em uma coleção do mongodb `pauloandre_limaflores`.  
  
As queries estão registradas no arquivo `queries.js`. Todas foram realizadas e verificadas utilizando o Mongo Shell ou o Compass.