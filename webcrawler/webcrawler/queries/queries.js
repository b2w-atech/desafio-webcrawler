// citações coletadas
dbo.luana_scardua.count()

// tags distintas
db.luana_scardua.distinct("tags")

// citações por autor
db.luana_scardua.aggregate(
    [{
        $group: {_id: "$author.name", qtd: {$sum: 1}}
    }])
    