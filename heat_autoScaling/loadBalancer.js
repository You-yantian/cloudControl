var cpu_util=db.meter.find({counter_name:"cpu_util",resource_id:"5b3fdfa5-8e05-4c61-b6dc-472a75adaf26"}).sort({timestamp:-1})
cpu_util.forEach(function(doc){db.temp_data.insert(doc)})