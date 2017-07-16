from time import sleep
for i in range(1,11,1):
	for j in range(1,11,1):
		result = i * j
		sleep(1)		
		print '%d * %d = %d' %(i,j,result)
	print 'multiple of %d completed.' %(i)
sleep(1)
print 'done'
