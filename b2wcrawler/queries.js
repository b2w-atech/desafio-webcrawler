//Quantas citações foram coletadas?
db.pauloandre_limaflores.count()

//Quantas tags distintas foram coletadas?
db.pauloandre_limaflores.distinct( "tags" )

//Quantas citações por autor foram coletadas? (exemplo abaixo)
db.pauloandre_limaflores.aggregate(
    [{
        $match: {

        }
    }, {
        $group: {
            _id: '$author.name',
            total: {
                '$sum': 1
            }
        }
    }]
)