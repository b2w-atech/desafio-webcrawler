// Question #1: How many quotes were collected?
// NOTE: official docs recommend avoiding `.count()` 2021-05-16 18:29:28
// https://docs.mongodb.com/manual/reference/method/db.collection.count/
db.ramon_melo.countDocuments({})

// Question #2: How many distinct tags were collected?
db.ramon_melo.distinct('tags').length

// Question #3: How many quotes per author were collected?
db.ramon_melo.aggregate([
    {
        $group: {
            _id: '$author.name',
            qtd: { $sum: 1 }
        }
    },
    {
        $sort: { qtd: -1 }
    }
])
