# Q2 q1
lst= range(0,10000)
f=open ("QuickSort.txt","r")
for x in range(0,10000):
	element=f.readline()
	lst[x]=int(element)
#print lst[9999]
f.close()

def partition(lst,l,r):
	p=lst[l]
	i=l+1
	for j in range(l+1,r+1):
		if lst[j] < p:
			c1= lst[j]
			lst[j]=lst[i]
			lst[i]=c
	c2= lst[l]
	lst[l]=lst[i-1]
	lst[i-1]= c2

#print len(lst)

def qst(lst, length):
	if length ==1:
		return lst
	else:
		p=lst[0]
		partition(lst,0,len(lst)-1)
		qst()


print qst(lst,len(lst))

