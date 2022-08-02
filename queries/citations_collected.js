result = db.jovane_mafort.aggregate(
    [
        // Count how many documents are inside the collection
        {
            $count: "number_of_citations_collected"
        }
    ]
).toArray();

printjson(result);