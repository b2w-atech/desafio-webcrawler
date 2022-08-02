result = db.jovane_mafort.aggregate(
    [
        // Deconstructs the tags array field
        {
            $unwind: "$tags"
        },
        // Group the documents by tags
        {
            $group: {_id: "$tags"}
        },
        // Counts the number of unique tags
        {
            $count: "number_of_distinct_tags"
        }
    ]
).toArray();

printjson(result);