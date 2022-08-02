result = db.jovane_mafort.aggregate(
    [
        // Groups and counts the documents by the name of each author
        {
            $group: { _id: "$author.name", quantity: { $count: {} } }
        },
        // Sort results by number of occurrences, descending
        {
            $sort: { quantity: -1}
        }
    ]
).toArray();

printjson(result);