#Sort the array elements in decreasing chronological order

DEBUG=True
def log(s):
	if DEBUG:
		print(s)
		
def date_higher(s1, s2):
	day1 =s1[0:2]
	month1 = s1[3:5]
	year1= s1[6:]
	
	day2 =s2[0:2]
	month2 = s2[3:5]
	year2= s2[6:]
	
	if year1 > year2:
		return True
	elif year1==year2 and month1 > month2:
		return True
	elif year1==year2 and month1==month2 and day1 >= day2:
		return True
	else:
		return False		

def merge(left,right):
	left_size = len(left)
	right_size = len(right)
	l = 0
	r = 0
	lst = []
	while(l < left_size and r <right_size):
		if (date_higher(left[l], right[r])):
			lst.append(left[l])
			l+=1
		else:
			lst.append(right[r])
			r+=1
			
	if l < left_size:
		lst = lst + left[l:]
	if r < right_size:
		lst = lst + right[r:]
	return lst
			
			
			
		
def msort(lst):
#termination condition
	lst_size = len(lst)
	if (lst_size <= 1):
		return lst
		
#recursive part
	else:
		half_size = int(lst_size/2)
		left = msort(lst[0:half_size])
		right = msort(lst[half_size:])
		lst_ret = merge(left,right)
	return lst_ret
		


lst =['01-05-2016', '05-08-2016', '07-09-2015', '02-24-2014', '09-30-2012', '01-09-2017']

log(date_higher('03-02-2017', '01-02-2017'))

lst_sorted = msort(lst)

log(lst_sorted)
