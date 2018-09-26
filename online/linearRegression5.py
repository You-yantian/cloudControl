import os
import numpy as np
import time
import csv

print "Start : %s" % time.ctime()
with open('linear4.csv','wb') as csvfile:
  writer=csv.writer(csvfile, delimiter=',')#, quotechar='|', quoting=csv.QUOTE_MINIMAL)
  for num in range(1,25):
	time.sleep(180)
	time_now = time.ctime()
	print "Sampling time : %s" % time_now
	W=np.array(([0.605551388264911],[-0.00495352031311974],
				 [0.005328950666037],[0.0000497242306728869],
				 [0.000186516968551362],[0.047749303477055]))

	output = os.popen('ceilometer statistics --meter cpu_util -p 180', 'r')
	text=output.read()
	x=text.split('|')
	cpu_util=float(x[len(x)-18])#6

	output = os.popen('ceilometer statistics --meter network.incoming.bytes.rate -p 180', 'r')
	text=output.read()
	x=text.split('|')
	networkIncomingRate=float(x[len(x)-18])/1024

	output = os.popen('ceilometer statistics --meter network.outgoing.bytes.rate -p 180', 'r')
	text=output.read()
	x=text.split('|')
	networkOutgoingRate=float(x[len(x)-18])/1024

	output = os.popen('ceilometer statistics --meter disk.device.write.bytes.rate -p 180', 'r')
	text=output.read()
	x=text.split('|')
	diskWriteBytesRate=float(x[len(x)-18])/1024

	output = os.popen('ceilometer statistics --meter disk.device.write.requests.rate -p 180', 'r')
	text=output.read()
	x=text.split('|')
	diskWriteRequestsRate=float(x[len(x)-18])

	output = os.popen('nova list', 'r')
	text=output.read()
	x=text.split('\n')
	num_server_now=len(x)-5

	print str(cpu_util)+' '+str(networkIncomingRate)+' '+str(networkOutgoingRate)+' '+str(diskWriteBytesRate)+' '+str(diskWriteRequestsRate)
	input_x=np.array([1,cpu_util,networkIncomingRate,networkOutgoingRate,diskWriteBytesRate,diskWriteRequestsRate])
	out_put=np.dot(input_x,W)
	num_server_predict=round(out_put)
	if num_server_predict>8:
		num_server_predict=8
	elif num_server_predict<1:
		num_server_predict=1
		
	print 'now: '+str(num_server_now)+' predict number: '+str(num_server_predict)
	
	if num_server_now < num_server_predict:
		while num_server_now < num_server_predict:
			os.popen('openstack server create --flavor m1.small --image CentOS \
				--nic net-id=053c1a03-c4f6-4995-907e-49f435693c3a --security-group default \
				--key-name private --user-data mydata.file webServer', 'w')
			num_server_now=num_server_now+1
	elif num_server_now > num_server_predict:
		while num_server_now > num_server_predict:
			output = os.popen('nova list', 'r')
			text = output.read()
			x = text.split('|')
			webServer_id = x[8]
			command = 'nova delete' + webServer_id
			os.popen(command, 'w')
			num_server_now=num_server_now-1
	print 'After prediction: '+str(num_server_now)
	
        writer.writerow([time_now, str(num_server_now)])
print "End : %s" % time.ctime()	
#openstack ip floating create admin_floating_net 




#openstack server create --flavor m1.small --image CentOS \
#			--nic net-id=053c1a03-c4f6-4995-907e-49f435693c3a --security-group default \
#			--key-name private --user-data mydata.file webServer
