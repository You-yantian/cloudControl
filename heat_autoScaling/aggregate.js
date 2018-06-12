db.getCollection("autoScaling").aggregate([

    	{    
         $project :{new_time_stamp :{$substr :["$timestamp",0,16]},counter_name:1,user_id:1,resource_id:1,timestamp:1,counter_volume:1}    
        }, 
        {    
         $match: {new_time_stamp:{$gt: "2018-06-11"}}    
    	}, 
    	{
    	  $group : {_id :"$new_time_stamp", count : {$sum:1} , avg:{$avg : "$counter_volume"}} 
    	}, 
    	])
