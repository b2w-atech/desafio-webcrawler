// Query to return how many quotes were collected in total
db.getCollection("diogo_castro").find({}).count();


// Query to return which distinct tags exist in the search
db.getCollection("diogo_castro").distinct("tags")


// Query to return how many distinct tags were collected
db.getCollection("diogo_castro").distinct("tags").length


// Query to return how many quotes per author were collected
db.getCollection("diogo_castro").aggregate({$group : { _id : '$author.name', qtd: {$sum : 1}}});
