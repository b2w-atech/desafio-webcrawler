// Quantas citações foram coletadas?
db.marcosvinicius_simoescampos.aggregate(
    [
        {$group: {_id: "$title"}},
        {$count: "quotes"}
    ]
)

// Quantas tags distintas foram coletadas?
db.marcosvinicius_simoescampos.aggregate(
    {$unwind: "$tags"},
    {$group: {_id: "$tags"}},
    {$count: "tags"}
)

// Quantas citações por autor foram coletadas?
db.marcosvinicius_simoescampos.aggregate(
    [
        {
            $group: {
                _id: "$author.name",
                qtd: {$sum: 1}
            }
        },
        {$sort: {qtd: -1}}
    ]
)