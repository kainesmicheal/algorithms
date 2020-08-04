def getNthFib(n):
	if n == 2:
		return 1
	elif n == 1:
		return 0
	else:
		return getNthFib(n-1) + getNthFib(n-2)
	
	#the time compexity is 0(2^n) as ever loop divides itself into two other calls
	#the space compexity is o(n) as there will be atmost n no. of funcition stack in a given moment
	
  def getNthFib(n, dump = {1:0,2:1}):
	if n in dump:
		return dump[n]
	else:
		dump[n] = getNthFib(n - 1, dump) + getNthFib(n - 2, dump)
		return dump[n]
	
#time complexity is o(n) as we have call the funtion time before all get into 
#the dump and the space complexity is o(n) as there will  be n no. of funtion calls
	
def getNthFib(n):
	base = [0,1]
	counter = 3
	while counter <= n:
		nextVal = base[0] + base[1]
		base[0] = base[1]
		base[1] = nextVal
		counter += 1
	if(n == 1):
		return base[0] 
	else:
		return base[1]
	
	#the time compexity is o(n) as we have to n operations and the space
	#compexity is o(1) as we not using anything other than a array of two values
