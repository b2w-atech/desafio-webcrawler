
    //Quantas citações por autor foram coletadas?
    db.alexander_parreira.aggregate([
    {$group: 
        {_id: '$author.name', 
            qtd:{$sum: 1}
        }
    },
    {$sort: {qtd: -1}       
        
    }]).pretty()


    //Quantas tags distintas foram coletadas?
    db.alexander_parreira.aggregate([ 
        {$unwind: {
            path:'$tag',
           }}, {$group: {
            _id: '$tag',
           }}, {$count: 'tag'}
    ]).pretty()

   //Quantas citações foram coletadas?
   db.alexander_parreira.aggregate([
       {$group: {
        _id: '$text',}
    }, {$count: 'tag'}])