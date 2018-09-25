import os
import numpy as np
import time
import csv

W1=np.array(([2.78934916,-1.666073695,0.663446406,-0.086863464],
			[2.424791007,1.624154671,-0.269592933,-2.983723794],
			[1.99168735,-0.342660718,1.02507826,1.809067655],
			[2.613879377,1.476116314,-1.899159848,-0.584317226],
			[2.698507028,2.583462324,1.870622943,2.439356924],
			[-2.739647382,-0.911742838,2.628835941,-3.037278432],
			[-2.237711361,-1.841896573,-1.866831573,0.643178469]))

W2=np.array(([0.330003018,-4.190669457,-4.329818878,1.064363463,-2.525406835],
			[2.795973493,-1.073309374,-0.10127491,1.501979284,-0.44423024],
			[-1.981678217,1.705665904,0.671396989,-3.898397906,-0.244925579],
			[1.570798022,0.151397775,-0.409252883,0.256048971,-1.453959067],
			[-0.490832169,-1.079228573,-0.004133946,-0.827848575,0.376001306]))

def  sigmoid(x):
    return 1.0 / (np.array(([1,1,1,1,1])) + np.exp(-x))
	
#def  tanh(x):
#	return 2*sigmoid(2*x) - 1
print "Start : %s" % time.ctime()
with open('linear1.csv','wb') as csvfile:
  writer=csv.writer(csvfile, delimiter=',')#, quotechar='|', quoting=csv.QUOTE_MINIMAL)
  for num in range(1,80):	
		output = os.popen('ceilometer statistics --meter cpu_util -p 180', 'r')
		text=output.read()
		x=text.split('|')
		cpu_util=float(x[len(x)-19])#7

		output = os.popen('ceilometer statistics --meter network.incoming.bytes.rate -p 180', 'r')
		text=output.read()
		x=text.split('|')
		networkIncomingRate=float(x[len(x)-19])


		output = os.popen('ceilometer statistics --meter network.outgoing.bytes.rate -p 360', 'r')
		text=output.read()
		x=text.split('|')
		networkOutgoingRate=float(x[len(x)-19])

		output = os.popen('ceilometer statistics --meter memory.usage -p 360', 'r')
		text=output.read()
		x=text.split('|')
		memoryUsage=float(x[len(x)-19])

		output = os.popen('ceilometer statistics --meter disk.device.write.bytes.rate -p 360', 'r')
		text=output.read()
		x=text.split('|')
		diskWriteBytesRate=float(x[len(x)-19])*2

		output = os.popen('ceilometer statistics --meter disk.device.write.requests.rate -p 360', 'r')
		text=output.read()
		x=text.split('|')
		diskWriteRequestsRate=float(x[len(x)-19])*2

		print str(cpu_util)+' '+str(networkIncomingRate)+' '+str(networkOutgoingRate)+' '+str(memoryUsage)+' '+str(diskWriteBytesRate)+' '+str(diskWriteRequestsRate)
		input_x=np.array([1,cpu_util,networkIncomingRate,networkOutgoingRate,memoryUsage,diskWriteBytesRate,diskWriteRequestsRate])
		hidden_layer=np.tanh(2*np.dot(input_x,W1)/3)*1.7159
		input_hidden=np.insert(hidden_layer,0,1,axis=0)
		#input_hidden=[1,hidden_layer]
		out_put=sigmoid(np.dot(input_hidden,W2))
		num_server_predict=np.argmax(out_put)+1;

		output = os.popen('nova list', 'r')
		text=output.read()
		x=text.split('\n')
		num_server_now=len(x)-5
		
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