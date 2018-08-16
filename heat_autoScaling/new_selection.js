var cpu_util=db.meter.find({counter_name:"cpu_util",project_id:"05825ebfbc60439b836886199af593ea"}).sort({timestamp:-1})
cpu_util.forEach(function(doc){db.temp_data.insert(doc)})
db.getCollection("temp_data").aggregate([
		{    
         $match: {new_time_stamp:{$gt: "2018-06-11"}}    
    	}, 
		{
    	  $out : "autoScaling"
    	}
    	])