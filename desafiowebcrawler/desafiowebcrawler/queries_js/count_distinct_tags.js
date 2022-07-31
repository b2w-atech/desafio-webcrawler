//Query para retornar o numero de tags recuperadas

var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("quotestoscrape");
    dbo.collection('matheus_ferreira').aggregate([
        {
            "$unwind": "$tag"
        },
        {
            "$group": {
                "_id": "$tag",
                "qtd": {
                    "$sum": 1
                }
            }
          },
        {
            "$sort": {qtd: -1, _id: 1}
        }
    ]).toArray().then(res => {
        res.forEach(post => console.log(JSON.stringify(post)));
    }).catch(err => {
        console.log(err)
    }).finally(() => {
        db.close();
    })
});
