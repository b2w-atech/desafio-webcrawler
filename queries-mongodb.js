//Quantas citações foram coletadas?
db.lucas_tavares.count()

//Quantas tags distintas foram coletadas?
db.lucas_tavares.aggregate( [
    
    { 
        $group: { _id: "$tags", 
                  "count": {"$sum":1} }
    },
    { $count: "count"}
    
 ] )

//Quantas citações por autor foram coletadas? (exemplo abaixo)
db.lucas_tavares.aggregate( [
    { 
        $group: { _id: "$author.name", 
                  "count": {"$sum":1} }
      },
      {
        $sort: {"count": -1}
      }
        
 ] )


