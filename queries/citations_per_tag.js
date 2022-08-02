result = db.jovane_mafort.aggregate(
    [
        // Deconstructs the tags array field
        {
            $unwind: "$tags",
        },
        // Group and counts the documents by each unique tag 
        {
            $group: { _id:"$tags", quantity: { $count: {} } }
        },
        // Sort results by number of occurrences, descending
        {
            $sort: { quantity: -1 } 
        }
    ]
).toArray();

printjson(result)