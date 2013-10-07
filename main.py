import os, random, copy

indexes = {}
predictions = {}
margin = 1
def learn():
	for files in os.listdir('Data'):
		f = open('Data/'+files, 'r')
		for line in f:
			try:
				items = line.split(',')
				avg = (float(items[2])+float(items[3])+float(items[4]))/3

				if items[0] in indexes:
					indexes[items[0]][3] += avg-indexes[items[0]][0]
					indexes[items[0]][3] /= 2
					if indexes[items[0]][0]>avg:
						indexes[items[0]][1] +=1
					else:
						indexes[items[0]][2] +=1

					indexes[items[0]][0]=avg
				else:
					indexes[items[0]]=[avg,0,0, 0]
			except Exception, e:
				pass
			
	for ticker in indexes:
		t = indexes[ticker][1]+indexes[ticker][2]	
		if t != 0:
			indexes[ticker][1] /= float(t)
			indexes[ticker][2] /= float(t)		

def predict(ticker, steps):
	temp = copy.deepcopy(indexes)
	#print 'Now: '+ticker+' - '+str(temp[ticker][0])
	if ticker in indexes:
		for i in range(0,steps):
			r = random.uniform(0, 99)
			if r > (100*indexes[ticker][1]):
				temp[ticker][0] += temp[ticker][3]
			else:
				temp[ticker][0] -= temp[ticker][3]
			
		#print 'In '+str(steps)+' days - '+str(temp[ticker][0])
		delta = float(temp[ticker][0]) - float(indexes[ticker][0]) 
		#print 'Delta: '+str(delta)
		return {ticker: [temp[ticker][0], delta]}

learn()
#for t in indexes:
#	predictions.update(predict(t, 1))

#s= sorted(predictions.items(), key=lambda x:x[1][1])
#print s[len(s)-1]
#print s[0]

print predict('FB', 3)
