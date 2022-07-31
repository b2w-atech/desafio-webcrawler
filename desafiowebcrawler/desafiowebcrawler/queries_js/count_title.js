//Query para retornar o numero de titulos recuperados

var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("quotestoscrape");
    dbo.collection('matheus_ferreira').aggregate([
    {
        "$count": "title"
    }]).toArray().then(function(result) {
        console.log("A quantidade de citações é: " + result[0].title)
    })
});

