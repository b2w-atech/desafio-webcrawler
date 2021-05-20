// Quantas citações foram coletadas?
db.joana_souza.count()

// Quantas tags distintas foram coletadas?
db.joana_souza.distinct("tags")

// Quantas citações por autor foram coletadas?
db.joana_souza.aggregate([{$group: {_id: "$author.name", qtd: {$sum: 1}}}])
