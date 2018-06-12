var cpu_util=db.meter.find({counter_name:"cpu_util",project_id:"05825ebfbc60439b836886199af593ea"}).sort({timestamp:-1})
cpu_util
cpu_util.forEach(function(doc){db.autoScaling.insert(doc)})