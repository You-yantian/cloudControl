var memo_usage=db.meter.find({counter_name:"memory.usage",project_id:"05825ebfbc60439b836886199af593ea"}).sort({timestamp:-1})
memo_usage.forEach(function(doc){db.temp_data.insert(doc)})
db.getCollection("temp_data").aggregate([

    	{    
         $project :{new_time_stamp :{$substr :["$timestamp",0,16]},counter_name:1,user_id:1,resource_id:1,timestamp:1,counter_volume:1}    
        }, 
        {    
         $match: {new_time_stamp:{$gt: "2018-06-11"}}    
    	}, 
    	{
    	  $group : {_id :"$new_time_stamp",  avg:{$avg : "$counter_volume"}} 
    	}, 
    	{
    	  $out : "collection"
    	}
    	])

db.autoScaling({},)    	